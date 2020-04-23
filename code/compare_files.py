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


def compare_files(corpus, filepath1, filepath2):
    database = fbhash.create_database(corpus)
    documents = database["documents"]
    weights = database["document_weights"]
    file1 = fbhash.Document(filepath1)
    file2 = fbhash.Document(filepath2)
    file1.digest(weights)
    file2.digest(weights)
    return cosine_distance(file1.digested_document, file2.digested_document)

if __name__ == '__main__':
    print(compare_files("../corpus", "../corpus/000060.html", "../corpus/000060.html"))
