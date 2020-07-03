"""
Problem 22:
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

NAMES_FILE = "../../resources/names.txt"

with open(NAMES_FILE, "r") as f:
    NAMES = [n.replace("\"", "") for n in f.readlines()[0].split(",")]


def answer():
    return sum((i + 1) * sum(ord(l) - 64 for l in n) for i, n in enumerate(sorted(NAMES)))


if __name__ == '__main__':
    print("Answer is:", answer())
