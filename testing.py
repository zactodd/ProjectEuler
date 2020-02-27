from memory_profiler import profile
from importlib import import_module
from timeit import timeit
import sys
from io import StringIO
import os
import matplotlib.pyplot as plt
from matplotlib import rc
import math

# rc('text', usetex=True)

ANSWERS_DIR = "Answers/"
with open("resources/problem_difficulty.txt") as f:
    DIFFICULT = [int(line.rstrip()) for line in f.readlines()]


def import_answer(answer_num):
    return import_module("Answers.answer{:03d}".format(answer_num)).answer


def test_answer_time(answer_num, tests=100):
    t = timeit(import_answer(answer_num), number=tests) / tests
    print(answer_num, t)
    return t


def test_answer_memory_usage(answer_num, tests=100):
    usages = []
    for _ in range(tests):
        previous_stdout = sys.stdout
        stream = StringIO()
        sys.stdout = stream
        profile(import_answer(answer_num), precision=10)()
        sys.stdout = previous_stdout
        print(stream.getvalue())
        output = stream.getvalue().split()
        usage = [float(output[i - 1]) for i, s in enumerate(output) if s == "MiB"]
        usages.append(usage[-2] - usage[0])
    print(answer_num, sum(usages) / len(usages))
    return sum(usages) / len(usages)


def answer_loc(answer_num):
    file = ANSWERS_DIR + "answer{:03d}.py".format(answer_num)
    with open(file, "r") as f:
        lines = f.readlines()
        return len(lines) - lines.index("\"\"\"\n", 1)


def answer_main_loc(answer_num):
    file = ANSWERS_DIR + "answer{:03d}.py".format(answer_num)
    with open(file, "r") as f:
        count = None
        for line in f.readlines():
            if line == "def answer():\n":
                count = 0
            elif count is not None:
                if line == "\n":
                    return count
                count += 1
        return 0


def visualise_answer_times(answers=range(1, 151), tests=100):
    times = [max(math.log10(test_answer_time(n, tests)), 0) for n in answers]
    min_a, max_a = min(answers), max(answers)
    bars = plt.bar(answers, times)
    log30, log60 = math.log10(30), math.log10(60)
    for b, t in zip(bars, times):
        if t > log60:
            b.set_color("red")
        elif t > log30:
            b.set_color("orange")
        else:
            b.set_color("green")
    plt.xlabel("Problems")

    plt.hlines(log60, 0, max_a + 1, colors="red")
    plt.hlines(log30, 0, max_a + 1, colors="orange")

    plt.ylabel("Time (max(log(s), 0)")
    plt.legend(["Max Expected Time (60s)", "Half Max Expected Time (30s)"])
    plt.xlim(min_a - 0.5, max_a + 0.5)
    plt.show()


def visualise_answer_memory(answers=range(1, 151), tests=100):
    usage = [test_answer_memory_usage(n, tests) for n in answers]
    min_a, max_a = min(answers), max(answers)
    bars = plt.bar(answers, usage)
    log30, log60 = math.log10(64), math.log10(128)
    for b, m in zip(bars, usage):
        if m > log60:
            b.set_color("red")
        elif m > log30:
            b.set_color("orange")
        else:
            b.set_color("green")
    plt.xlim(min_a - 0.5, max_a + 0.5)
    plt.hlines(math.log(128, 2), 0, max_a + 1, colors="red")
    plt.hlines(math.log(64, 2), 0, max_a + 1, colors="orange")
    plt.xlabel("Problems")
    plt.ylabel("Memory (max(log2(MiB), 0)")
    plt.legend(["Max Expected Memory Used (128 MiB)", "Half Max Expected Memory Used (64 MiB)"])
    plt.xlim(min_a - 0.5, max_a + 0.5)
    plt.show()


def visualise_answer_loc(answers=range(1, 151)):
    main_loc = [answer_main_loc(n) for n in answers]
    lines = [answer_loc(n) for n in answers]
    min_a, max_a = min(answers), max(answers)
    p1 = plt.bar(answers, lines)
    p2 = plt.bar(answers, main_loc)
    plt.legend((p1[0], p2[0]), ("Total SRC LOC", "answer() LOC"))
    plt.xlabel("Problems")
    plt.ylabel("LOC")
    plt.xlim(min_a - 0.5, max_a + 0.5)
    plt.show()


def visualise_answer_difficulty(answers=range(1, 151)):
    plt.bar(answers, [DIFFICULT[a - 1] for a in answers])
    min_a, max_a = min(answers), max(answers)
    plt.xlabel("Problems")
    plt.ylabel("%")
    plt.xlim(min_a - 0.5, max_a + 0.5)
    plt.show()


visualise_answer_loc()
