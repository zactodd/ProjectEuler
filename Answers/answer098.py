"""
Question 98:
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
"""
from itertools import permutations, combinations

WORDS_FILE = "../resources/words.txt"
with open(WORDS_FILE, "r") as f:
    WORDS = [(w[1:-1], sorted(w[1:-1])) for w in f.readlines()[0].split(",")]


def sq(n, letters, y):

    x = int("".join(str(y[letters[i]]) for i in n))
    return x if int(x ** 0.5) ** 2 == x else False


def answer():
    pairs = [(w1, w2) for (w1, s1), (w2, s2) in combinations(WORDS, 2) if s1 == s2]

    max_sq = 0
    for w, a in pairs:
        letters = {x: y for y, x in enumerate(set(w))}
        for y in permutations(range(1, 10), len(letters)):
            if (cw := sq(w, letters, y)) and (ca := sq(a, letters, y)):
                max_sq = max(cw, ca, max_sq)
    return max_sq


if __name__ == '__main__':
    print("Answer is:", answer())
