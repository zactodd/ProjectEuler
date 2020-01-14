"""
Problem 149:
Looking at the table below, it is easy to verify that the maximum possible sum of adjacent numbers in any direction (horizontal, vertical, diagonal or anti-diagonal) is 16 (= 8 + 7 + 1).

−2	5	3	2
9	−6	5	1
3	2	7	3
−1	8	−4	  8
Now, let us repeat the search, but on a much larger scale:

First, generate four million pseudo-random numbers using a specific form of what is known as a "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, sk = [100003 − 200003k + 300007k3] (modulo 1000000) − 500000.
For 56 ≤ k ≤ 4000000, sk = [sk−24 + sk−55 + 1000000] (modulo 1000000) − 500000.

Thus, s10 = −393027 and s100 = 86613.

The terms of s are then arranged in a 2000×2000 table, using the first 2000 numbers to fill the first row (sequentially), the next 2000 numbers to fill the second row, and so on.

Finally, find the greatest sum of (any number of) adjacent entries in any direction (horizontal, vertical, diagonal or anti-diagonal).
"""


def answer():
    def max_sub_sum(x, y, dx, dy):
        result = 0
        current = 0
        while 0 <= x < size and 0 <= y < size:
            current = max(current + grid[y][x], 0)  #
            result = max(current, result)
            x += dx
            y += dy
        return result

    size = 2000
    seq = []
    for i in range(1, size ** 2 + 1):
        if i <= 55:
            seq.append((100003 - 200003 * i + 300007 * i ** 3) % 1000000 - 500000)
        else:
            seq.append((seq[-24] + seq[-55]) % 1000000 - 500000)
    grid = [seq[i * size: (i + 1) * size] for i in range(size)]
    return max(
        max(
            max_sub_sum(0, i, +1, 0), max_sub_sum(i, 0, 0, +1), max_sub_sum(0, i, +1, +1),
            max_sub_sum(i, 0, +1, +1), max_sub_sum(i, 0, -1, +1), max_sub_sum(size - 1, i, -1, +1)
        ) for i in range(size))


if __name__ == '__main__':
    print("Answer is:", answer())
