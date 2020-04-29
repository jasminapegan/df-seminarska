import glob
import os
import random
from matplotlib import pyplot as plt

from compare_files import compare_files


def generate_test_files(matching, filepath1, filepath2, target):
    file1 = ""
    file2 = ""
    with open(filepath1, 'rb') as file:
        file1 = file.read()
    with open(filepath2, 'rb') as file:
        file2 = file.read()

    output = ""
    if matching != 1:
        required_file2 = int(matching * len(file1) / (1 - matching))
    if matching == 1 or required_file2 > len(file2):
        required_file1 = int((1 - matching) * len(file2) / matching)
        start_of_chunk = random.randint(0, len(file2) - 1)
        chunk_location = random.randint(0, len(file1) - required_file1 - 1)
        output = file2[:start_of_chunk] + file1[chunk_location: chunk_location + required_file1] + file2[
                                                                                                   start_of_chunk:]
    else:
        start_of_chunk = random.randint(0, len(file1) - 1)
        chunk_location = random.randint(0, len(file2) - required_file2 - 1)
        output = file1[:start_of_chunk] + file2[chunk_location: chunk_location + required_file2] + file1[
                                                                                                   start_of_chunk:]

    with open(target, 'wb') as file:
        file.write(output)


def standard_test(corpus):
    file_names = [f for f in glob.glob(corpus + "/**", recursive=True) if not os.path.isdir(f)]
    percents = []
    score = []
    similarities = []
    tries = 100
    steps = [100,90,80,70,60,50,40,30,20,10,5,4,3,2,1]
    # steps = range(100, 0, -1)
    for p in steps:
        print("Testing", p, "%")
        detections = 0
        avg_sim = 0
        for i in range(tries):
            fileA = file_names[random.randint(0, len(file_names) - 1)]
            fileB = file_names[random.randint(0, len(file_names) - 1)]
            while fileA == fileB:
                fileB = file_names[random.randint(0, len(file_names) - 1)]
            generate_test_files(p / 100, fileA, fileB, corpus + "tmp")
            similarity = compare_files(corpus, fileB, corpus + "tmp")
            avg_sim += similarity
            if similarity > 0.005:
                detections += 1
        avg_sim /= tries
        percents.append(str(p) + "%")
        score.append(100 * detections / tries)
        similarities.append(avg_sim)
    os.remove(corpus + "tmp")

    # drawing a plot
    fig, ax1 = plt.subplots()
    ax1.plot(percents, score, 'b-')
    ax1.set_xlabel("Odstotek ujemanja")
    ax1.set_ylabel("Zaznano")
    ax1.set_ylim(0, 110)

    ax2 = ax1.twinx()
    ax2.bar(percents, similarities, align='center', alpha=0.5)
    ax2.set_ylabel('Ocena ujemanja')
    ax2.set_ylim(0, 1.1)
    ax2.tick_params('y')

    plt.title("Zaznava ujemanja")
    plt.show()


if __name__ == '__main__':
    standard_test("../corpus")
