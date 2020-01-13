from memory_profiler import profile
from importlib import import_module
from timeit import timeit
import sys
from io import StringIO

ANSWERS_DIR = "Answers/"


def import_answer(answer_num):
    return import_module("Answers.answer{:03d}".format(answer_num)).answer


def test_answer_time(answer_num, tests=100):
    return timeit(import_answer(answer_num), number=tests)


def test_answer_memory_usage(answer_num, tests=100):
    usages = []
    for _ in range(tests):
        previous_stdout = sys.stdout
        stream = StringIO()
        sys.stdout = stream
        profile(import_answer(answer_num), precision=10)()
        sys.stdout = previous_stdout
        output = stream.getvalue().split()
        total_usage = [float(output[i - 1]) for i, s in enumerate(output) if s == "MiB"][-2]
        usages.append(total_usage)
    return sum(usages) / len(usages)
