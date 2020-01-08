"""
Question 119:
Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets can be formed. Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?
"""


def digits_sum(n):
    return sum(map(int, str(n)))


def answer():
    n = 30
    a = []
    for b in range(2, 100):
        a.extend([p for e in range(2, 10) if digits_sum(p := (b ** e)) == b])
    return sorted(a)[n - 1]


if __name__ == '__main__':
    print("Answer is:", answer())
