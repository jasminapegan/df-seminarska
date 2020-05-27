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
        if len(file2) - required_file2 - 1 <= 0:
            chunk_location = 0
        else:
            chunk_location = random.randint(0, len(file2) - required_file2 - 1)
        output = file1[:start_of_chunk] + file2[chunk_location: chunk_location + required_file2] + file1[
                                                                                                   start_of_chunk:]

    with open(target, 'wb') as file:
        file.write(output)


def f_score(corpus):
    file_names = [f for f in glob.glob(corpus + "/**", recursive=True) if not os.path.isdir(f)]
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    tries = 500
    for test in range(tries):
        print(test)
        fileA = file_names[random.randint(0, len(file_names) - 1)]
        fileB = file_names[random.randint(0, len(file_names) - 1)]
        while fileA == fileB:
            fileB = file_names[random.randint(0, len(file_names) - 1)]
        if bool(random.getrandbits(1)):
            generate_test_files(random.randint(1, 100) / 100, fileA, fileB, corpus + "/tmp")
            if compare_files(corpus, fileB, corpus + "/tmp") >= 0.01:
                tp+=1
            else:
                fn+=1
        else:
            generate_test_files(0, fileA, fileB, corpus + "/tmp")
            if compare_files(corpus, fileB, corpus + "/tmp") >= 0.01:
                fp += 1
            else:
                tn += 1
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    fscore = 2*(precision*recall)/(precision+recall)
    print("precision:", precision)
    print("recall:", recall)
    print("f-score:", fscore)
    os.remove(corpus + "/tmp")

def standard_test(corpus):
    file_names = [f for f in glob.glob(corpus + "/**", recursive=True) if not os.path.isdir(f)]
    percents = []
    score = []
    similarities = []
    tries = 100
    steps = [100,80,60,40,20,10,6,3,1]
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
            generate_test_files(p / 100, fileA, fileB, corpus + "/tmp")
            similarity = compare_files(corpus, fileB, corpus + "/tmp")
            avg_sim += similarity
            if similarity >= 0.01:
                detections += 1
        avg_sim /= tries
        percents.append(str(p) + "%")
        score.append(100 * detections / tries)
        similarities.append(avg_sim)
    os.remove(corpus + "/tmp")

    # drawing a plot
    font = {'family': 'DejaVu Sans',
            'weight': 'bold',
            'size': 12}
    plt.rc('font', **font)
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
    # standard_test("../corpus")
    f_score("../corpus")
