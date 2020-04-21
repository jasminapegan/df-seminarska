import sys


class ByteTable:
    def __init__(self, k):
        self.bt = [0]*k
        self.p = 0
        self.k = k

    def insert(self, b):
        self.bt[self.p] = b
        self.p = (self.p + 1) % self.k

    def get(self):
        return self.bt[self.p]


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
            rol_hash = (a*rol_hash + num) % n
        hashes.append(rol_hash)
        ak = a**k
        while True:
            byte = file.read(1)
            if not byte:
                return hashes
            num = int.from_bytes(byte, 'big')
            rol_hash = rolling_hash(rol_hash, byte_table.get(), num, a, ak, n)
            byte_table.insert(num)
            hashes.append(rol_hash)


def rolling_hash(prev_hash, b0, bk, a, ak, n):
    return (a*prev_hash - b0*ak + bk) % n


def hash_a_file(filename):
    chunk_hashes = file_to_chunks(filename, 2, 100, 7)
    return 0


if __name__ == '__main__':
    hash_a_file(sys.argv[1])
