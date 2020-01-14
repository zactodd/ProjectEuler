"""
Problem 103:
Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
If S(A) is minimised for a given n, we shall call it an optimum special sum set. The first five optimum special sum sets are given below.

n = 1: {1}
n = 2: {1, 2}
n = 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}

It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.

By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: 111819202225.

Given that A is an optimum special sum set for n = 7, find its set string.

NOTE: This problem is related to Problem 105 and Problem 106.
"""


def lex_lowest(t, max_sum):
    def recur(set_info, size, s, start=1):
        if size == 0:
            return set_info
        elif size >= 2 and start * size >= s:
            return None
        values = set_info[0]
        end = s
        if len(values) >= 2:
            end = min(values[0] + values[1] - 1, end)
        for val in range(start, end + 1):
            if (candidate := update(val, set_info)) is None:
                continue
            elif (candidate := recur(candidate, size - 1, s - val, val + 1)) is not None:
                return candidate
        else:
            return None
    initial = ([], [True], [0], [0])
    return recur(initial, t, max_sum)


def update(val, set_info):
    values, posb, min_sum, max_sum = set_info
    size = len(values)
    if any((posb[i] and posb[i - val]) for i in range(val, len(posb))):
        return None

    candidate_size = size + 1
    candidate_min = [0] + [min(min_sum[i], min_sum[i - 1] + val)
                           for i in range(1, candidate_size)] + [min_sum[size] + val]
    candidate_max = [0] + [max(max_sum[i], max_sum[i - 1] + val)
                           for i in range(1, candidate_size)] + [max_sum[size] + val]

    if any((candidate_max[i] >= candidate_min[i + 1]) for i in range(candidate_size)):
        return None

    candidate_posb = posb + [False] * val
    for i in reversed(range(val, len(candidate_posb))):
        candidate_posb[i] |= candidate_posb[i - val]
    if (u := (values + [val], candidate_posb, candidate_min, candidate_max)) is None:
        return None
    else:
        return u


def answer():
    size, max_sum = 7, 1
    while lex_lowest(size, max_sum) is None:
        max_sum *= 2
    i = max_sum // 4
    while i > 0:
        max_sum += i if lex_lowest(size, max_sum - 1) is None else - 1
        i //= 2
    values, *_ = lex_lowest(size, max_sum)
    return int("".join(map(str, values)))


if __name__ == '__main__':
    print("Answer is:", answer())
