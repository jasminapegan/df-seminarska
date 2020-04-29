import fbhash
import os
from zipfile import ZipFile
from mimetypes import guess_type


def cosine_distance(digested_document1, digested_document2):
    keys_intersection = set(digested_document1.keys()) & set(digested_document2.keys())
    scalar_product = 0
    for key in keys_intersection:
        scalar_product += digested_document1[key] * digested_document2[key]

    vector_size1 = 0
    for key in digested_document1.keys():
        vector_size1 += digested_document1[key] ** 2
    vector_size1 **= (1 / 2)

    vector_size2 = 0
    for key in digested_document2.keys():
        vector_size2 += digested_document2[key] ** 2
    vector_size2 **= (1 / 2)

    return scalar_product / (vector_size1 * vector_size2)


cached_corpus = ""
cached_weights = []

def compare_files(corpus, filepath1, filepath2):
    global cached_corpus, cached_weights
    if corpus != cached_corpus:
        database = fbhash.create_database(corpus)
        documents = database["documents"]
        weights = database["document_weights"]
        cached_weights = weights
        cached_corpus = corpus
    file1 = fbhash.Document(filepath1)
    file2 = fbhash.Document(filepath2)
    file1.digest(cached_weights)
    file2.digest(cached_weights)
    return cosine_distance(file1.digested_document, file2.digested_document)


def delete_dir(dir):
    for item in os.listdir(dir):
        if os.path.isdir(item):
            delete_dir(item)
        else:
            os.remove(os.path.join(dir, item))
    os.rmdir(dir)


def generate_files_in_dir(dir, path=""):
    for item in os.listdir(dir):
        if os.path.isdir(item):
            generate_files_in_dir(item, path=dir)
        else:
            yield os.path.join(path, dir, item)


def compare_zip_files(corpus, filepath1, filepath2, tmpdir="tmp"):
    cwd = os.getcwd()
    root_dir = os.path.join(cwd, tmpdir)
    tmpdir_f1, tmpdir_f2 = os.path.join(cwd, tmpdir, "f1"), os.path.join(cwd, tmpdir, "f2")
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
    os.mkdir(tmpdir_f1)
    os.mkdir(tmpdir_f2)

    with ZipFile(filepath1, "r") as zf:
        zf.extractall(tmpdir_f1)
    with ZipFile(filepath2, "r") as zf:
        zf.extractall(tmpdir_f2)

    scores = []
    for f1 in generate_files_in_dir(tmpdir_f1):
        for f2 in generate_files_in_dir(tmpdir_f2):
            print(f1 + ", " + f2 + "\n")
            _, ext1 = os.path.splitext(f1)
            _, ext2 = os.path.splitext(f2)
            type = str(guess_type(f1))
            print(str(type))
            if ext1 == ext2 and ("image" in type or "text" in type):
                scores.append(compare_files(corpus, f1, f2))

    print(scores)
    delete_dir(root_dir)
    if scores:
        return sum(scores) / len(scores)
    else:
        return 0.


if __name__ == '__main__':
    print(compare_files("../corpus", "../corpus/000060.html", "../corpus/000060.html"))
    # testni datoteki a.zip in b.zip, lahko se pobrišejo ko se ne rabjo več
    # print(compare_zip_files("../corpus", "../corpus/a.zip", "../corpus/b.zip"))
