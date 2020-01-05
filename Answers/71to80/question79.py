"""
Question 79:
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""

from itertools import count
SEQ = [
    '319', '680', '180', '690', '129', '620', '762', '689', '762', '318', '368', '710', '720', '710', '629', '168',
    '160', '689', '716', '731', '736', '729', '316', '729', '729', '710', '769', '290', '719', '680', '318', '389',
    '162', '289', '162', '718', '729', '319', '790', '680', '890', '362', '319', '760', '316', '729', '380', '319',
    '728', '716'
]


def is_subsequence(short, long):
    i = 0
    return any(c == short[i] and (i := (i + 1)) == len(short) for c in long)


def answer():
    chars = sorted(set(SEQ))
    base = len(chars)
    for length in count(base):
        inds = [0] * length
        while True:
            guess = "".join(chars[d] for d in inds)
            if all(is_subsequence(s, guess) for s in SEQ):
                return guess
            i = 0
            while i < length and inds[i] == base - 1:
                inds[i] = 0
                i += 1
            if i == length:
                break
            inds[i] += 1


if __name__ == '__main__':
    print("Answer is:", answer())



