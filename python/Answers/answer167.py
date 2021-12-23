
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


if __name__ == '__main__':
    print(answer())