"""
Problem 167:
For two positive integers a and b, the Ulam sequence U(a,b) is defined by U(a,b)1 = a, U(a,b)2 = b and for k > 2, U(a,b)k is the smallest integer greater than U(a,b)(k-1) which can be written in exactly one way as the sum of two distinct previous members of U(a,b).

For example, the sequence U(1,2) begins with
1, 2, 3 = 1 + 2, 4 = 1 + 3, 6 = 2 + 4, 8 = 2 + 6, 11 = 3 + 8;
5 does not belong to it because 5 = 1 + 4 = 2 + 3 has two representations as the sum of two previous members, likewise 7 = 1 + 6 = 3 + 4.

Find ∑ U(2,2n+1)k for 2 ≤ n ≤10, where k = 1011.
"""


def answer(k=10 ** 11):
    periods = [32, 26, 444, 1628, 5906, 80, 126960, 380882, 2097152]  # A100729
    differences = [126, 126, 1778, 6510, 23622, 510, 507842, 1523526, 8388606]  # A100730

    def ulm(n, term):
        t = n + 5
        period, difference = periods[n - 2], differences[n - 2]
        q, r = divmod(term - t, period)
        even_term1, even_term2 = 2, 4 * n + 4
        odd_terms = set([2 * i + 1 for i in range(n, 2 * n + 2)])
        c, d = 0, 4 * n + 5
        while True:
            if (d - even_term1 in odd_terms) ^ (d - even_term2 in odd_terms):
                if c == r:
                    return q * difference + d
                odd_terms.add(d)
                c += 1
            d += 2
    return sum([ulm(n, k) for n in range(2, 10 + 1)])


if __name__ == "__main__":
    print("Answer is:", answer())

