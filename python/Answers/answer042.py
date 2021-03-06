"""
Problem 42:

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""


WORDS_FILE = "../../resources/words.txt"
TRIANGLES = [t * (t + 1) // 2 for t in range(100)]

with open(WORDS_FILE, "r") as f:
    WORDS = [n.replace("\"", "") for n in f.readlines()[0].split(",")]


def answer(triangles=TRIANGLES, words=WORDS):
    return sum(sum(ord(l) - 64 for l in w) in triangles for w in words)


if __name__ == '__main__':
    print("Answer is:", answer())
