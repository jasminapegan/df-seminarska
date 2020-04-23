import random


def generate_test_files(matching, filepath1, filepath2, target):
    file1 = ""
    file2 = ""
    with open(filepath1, 'rb') as file:
        file1 = file.read()
    with open(filepath2, 'rb') as file:
        file2 = file.read()

    output = ""
    required_file2 = int(matching * len(file1) / (1 - matching))
    if required_file2 > len(file2):
        required_file1 = int((1 - matching) * len(file2) / matching)
        start_of_chunk = random.randint(0, len(file2))
        chunk_location = random.randint(0, len(file1) - required_file1)
        output = file2[:start_of_chunk] + file1[chunk_location: chunk_location + required_file1] + file2[start_of_chunk:]
    else:
        start_of_chunk = random.randint(0, len(file1))
        chunk_location = random.randint(0, len(file2) - required_file2)
        output = file1[:start_of_chunk] + file2[chunk_location: chunk_location + required_file2] + file1[start_of_chunk:]

    with open(target, 'wb') as file:
        file.write(output)



if __name__ == '__main__':
    generate_test_files(0.3, "../corpus/000060.html", "../corpus/000083.text", "izhod.txt")
