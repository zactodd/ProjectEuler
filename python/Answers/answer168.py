def answer(m=10 ** 5):
    return sum(10 * x + y for k in range(1, 100) for d in range(1, 10)
               for y, (x, r) in map(lambda y: (y, divmod((10 ** k - d) * y, 10 * d - 1)), range(1, 10))
               if r == 0 and x >= 10 ** (k - 1)) % m

