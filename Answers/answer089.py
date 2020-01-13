"""
Question 89:
For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
"""

ROMAN_FILE = "../resources/roman.txt"
with open(ROMAN_FILE, "r") as f:
    NOT_SIMPLE_ROMAN = "".join(f.readlines()).split("\n")

ROMAN_PREFIXES = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
]

LENGTHS = [0, 1, 2, 3, 2, 1, 2, 3, 4, 2]


def parse_roman(s):
    result = 0
    while len(s) > 0:
        for (prefix, val) in ROMAN_PREFIXES:
            if s.startswith(prefix):
                result += val
                s = s[len(prefix):]
                break
    return result


def roman_numeral_len(n):
    assert 1 < n < 5000
    l = 0
    if n >= 4000:
        l += 2
    while n > 0:
        l += LENGTHS[n % 10]
        n //= 10
    return l


def answer():
    return sum(len(s) - roman_numeral_len(parse_roman(s)) for s in NOT_SIMPLE_ROMAN)


if __name__ == '__main__':
    print("Answer is:", answer())
