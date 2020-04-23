import fbhash


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

if __name__ == '__main__':
    print(compare_files("../corpus", "../corpus/000060.html", "../corpus/000060.html"))
