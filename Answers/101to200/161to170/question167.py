"""
Question 167:
For two positive integers a and b, the Ulam sequence U(a,b) is defined by U(a,b)1 = a, U(a,b)2 = b and for k > 2, U(a,b)k is the smallest integer greater than U(a,b)(k-1) which can be written in exactly one way as the sum of two distinct previous members of U(a,b).

For example, the sequence U(1,2) begins with
1, 2, 3 = 1 + 2, 4 = 1 + 3, 6 = 2 + 4, 8 = 2 + 6, 11 = 3 + 8;
5 does not belong to it because 5 = 1 + 4 = 2 + 3 has two representations as the sum of two previous members, likewise 7 = 1 + 6 = 3 + 4.

Find ∑ U(2,2n+1)k for 2 ≤ n ≤10, where k = 1011.
"""


def period_term(n, which_one):
    first_even_term = 2
    second_even_term = 4 * n + 4
    odd_terms = set([2 * i + 1 for i in range(n, 2 * n + 2)])

    d = 4 * n + 5
    count = 0
    while True:
        if (d - first_even_term in odd_terms) ^ (d - second_even_term in odd_terms):
            if count == which_one:
                return d
            odd_terms.add(d)
            count += 1
        d += 2


def answer():
    periods = [32, 26, 444, 1628, 5906, 80, 126960, 380882, 2097152]
    differences = [126, 126, 1778, 6510, 23622, 510, 507842, 1523526, 8388606]

    def u(n, which_term):
        t = n + 5
        period = periods[n - 2]
        difference = differences[n - 2]
        q, r = divmod(which_term - t, period)
        return q * difference + period_term(n, r)

    return sum([u(n, 10 ** 11) for n in range(2, 10 + 1)])


if __name__ == '__main__':
    print("Answer is:", answer())
