import sys
import os
import glob
import math
from collections import Counter
from itertools import chain


def file_to_chunks(filename, a, n, k):
    with open(filename, 'rb') as file:
        rol_hash = 0
        hashes = []
        byte_table = ByteTable(k)
        for i in range(k):
            byte = file.read(1)
            if not byte:
                return hashes
            num = int.from_bytes(byte, 'big')
            byte_table.insert(num)
            rol_hash = (a * rol_hash + num) % n
        hashes.append(rol_hash)
        ak = a ** k
        while True:
            byte = file.read(1)
            if not byte:
                return hashes
            num = int.from_bytes(byte, 'big')
            rol_hash = rolling_hash(rol_hash, byte_table.get(), num, a, ak, n)
            byte_table.insert(num)
            hashes.append(rol_hash)


def rolling_hash(prev_hash, b0, bk, a, ak, n):
    return (a * prev_hash - b0 * ak + bk) % n


class ByteTable:
    def __init__(self, k):
        self.bt = [0] * k
        self.p = 0
        self.k = k

    def insert(self, b):
        self.bt[self.p] = b
        self.p = (self.p + 1) % self.k

    def get(self):
        return self.bt[self.p]


class Document:
    def __init__(self, filename: str):
        self.params = DocParams()
        chunks = file_to_chunks(filename, self.params.a, self.params.n, self.params.k)
        self.chunk_freq = Counter(chunks)
        self.weights = self.params.calculate_weights(self.chunk_freq, len(chunks))
        self.digested_document = None

    def document_terms(self):
        return list(self.chunk_freq)

    def digest(self, document_weights):
        self.digested_document = {c: (self.weights[c] * document_weights.get(c, 1.0)) for c in
                                  list(self.weights.keys())}


def create_database(folder_name: str):
    file_names = [f for f in glob.glob(folder_name + "/**", recursive=True) if not os.path.isdir(f)]
    documents = {f: Document(f) for f in file_names}
    chunk_document_freq = Counter(chain.from_iterable([d.document_terms() for d in documents.values()]))
    chunk_document_weight = document_weight(chunk_document_freq, len(file_names))
    for d in documents.keys():
        documents[d].digest(chunk_document_weight)
    return {"document_weights": chunk_document_weight, "documents": documents}


# Chunk frequency weighting functions inside the document


def ch_tfidf_weight(element_freq: Counter, chunk_num: int):
    return {c: (math.log2(1 + element_freq[c] / chunk_num)) for c in list(element_freq)}


def ch_tfidf_weight_clanek(element_freq: Counter, chunk_num: int):
    return {c: (1 + math.log10(element_freq[c] / chunk_num)) for c in list(element_freq)}


def ch_freq_weight(element_freq: Counter, chunk_num: int):
    return {c: (element_freq[c] / chunk_num) for c in list(element_freq)}


def ch_log_weight(element_freq: Counter, chunk_num: int):
    return {c: (math.log2(element_freq[c] / chunk_num)) for c in list(element_freq)}


# Document chunk frequency weighting functions


def doc_log_weigh(document_freq: Counter, doc_num: int):
    return {c: (math.log10(doc_num / document_freq[c])) for c in list(document_freq)}


def doc_norm_weigh(document_freq: Counter, doc_num: int):
    return {c: (1 - math.log10(document_freq[c] / doc_num)) for c in list(document_freq)}


class DocParams:
    def __init__(self):
        self.k = 7  # from equation
        self.n = 2793861040361076437  # random prime number 2^54 < n < 2^64
        self.a = 97  # constant 0 < a < 256
        self.calculate_weights = ch_tfidf_weight_clanek


document_weight = doc_log_weigh

if __name__ == '__main__':
    create_database(sys.argv[1])
