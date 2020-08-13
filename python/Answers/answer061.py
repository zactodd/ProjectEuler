"""
Problem 61:
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:

Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	 	P4,n=n2	 	1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
"""


def fn(n):
    return (3, n * (n + 1) / 2), \
           (4, n * n), \
           (5, n * (3 * n - 1) / 2), \
           (6, n * (2 * n - 1)), \
           (7, n * (5 * n - 3) / 2), \
           (8, n * (3 * n - 2))


def chain(types, data, ds):
    return sum(data) if len(types) == 6 and data[0] // 100 == data[-1] % 100 else \
        next((chain(types + [t], data + [n], ds) for t, n in ds.get((types[-1], data[-1]), []) if t not in types), None)


def answer():
    poly_nums = [(t, d) for n in range(19, 141) for t, d in fn(n) if 1000 <= d <= 9999 and d % 100 > 9]
    ds = {}
    for t1, d1 in poly_nums:
        for t2, d2 in poly_nums:
            if t1 != t2 and d1 % 100 == d2 // 100:
                ds[(t1, d1)] = ds.get((t1, d1), []) + [(t2, d2)]
    return next(int(s) for t, d in ds if (s := chain([t], [d], ds)) is not None)


if __name__ == '__main__':
    print("Answer is:", answer())
