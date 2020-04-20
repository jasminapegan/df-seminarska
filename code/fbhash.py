import sys


def file_to_bin(filename):
    with open(filename, 'rb') as file:
        data = ['{0:08b}'.format(val) for val in bytearray(file.read())]
        return "".join(data)


def hash_a_file(filename):
    binary_sequence = file_to_bin(filename)
    return 0


if __name__ == '__main__':
    hash_a_file(sys.argv[1])
