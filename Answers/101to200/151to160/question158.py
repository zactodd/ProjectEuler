"""
Question 158:
Taking three different letters from the 26 letters of the alphabet, character strings of length three can be formed.
Examples are 'abc', 'hat' and 'zyx'.
When we study these three examples we see that for 'abc' two characters come lexicographically after its neighbour to the left.
For 'hat' there is exactly one character that comes lexicographically after its neighbour to the left. For 'zyx' there are zero characters that come lexicographically after its neighbour to the left.
In all there are 10400 strings of length 3 for which exactly one character comes lexicographically after its neighbour to the left.

We now consider strings of n ≤ 26 different characters from the alphabet.
For every n, p(n) is the number of strings of length n for which exactly one character comes lexicographically after its neighbour to the left.

What is the maximum value of p(n)?
"""


def answer():
    factorial = {0: 1}
    for i in range(1, 27):
        factorial[i] = factorial[i - 1] * i

    dp = {(0, 0, 0): 0, (0, 0, 1): 1}

    def n(l, max_n, c):
        if (l, max_n, c) not in dp:
            r = sum(n(l - 1, i, c + ((i < max_n) and 1 or 0)) for i in range(l))
            dp[(l, max_n, c)] = r
        return dp[(l, max_n, c)]

    def p(x):
        return sum(n(x - 1, i, 0) for i in range(x)) * (factorial[26] // (factorial[x] * factorial[26 - x]))

    return max(p(n) for n in range(2, 27))


if __name__ == '__main__':
    print("Answer is:", answer())
