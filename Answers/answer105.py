"""
Problem 105:
Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair combinations and S(A) = 1286.

Using sets.txt (right click and "Save Link/Target As..."), a 4K text file with one-hundred sets containing seven to twelve elements (the two examples given above are the first two sets in the file), identify all the special sum sets, A1, A2, ..., Ak, and find the value of S(A1) + S(A2) + ... + S(Ak).

NOTE: This problem is related to Problem 103 and Problem 106.
"""


SETS_FILE = "../resources/sets.txt"
with open(SETS_FILE, "r") as f:
    SETS = [list(map(int, line.split(","))) for line in f.readlines()]


def is_special(s):
    found = set()
    max_sum = [float("-Inf")] * (len(s) + 1)
    min_sum = [float("Inf")] * (len(s) + 1)

    def recur_subsets(i, count, ssum):
        if i == len(s):
            found.add(ssum)
            if ssum > max_sum[count]:
                max_sum[count] = ssum
            elif ssum < min_sum[count]:
                min_sum[count] = ssum
        else:
            recur_subsets(i + 1, count, ssum)
            recur_subsets(i + 1, count + 1, ssum + s[i])
    recur_subsets(0, 0, 0)
    return len(found) == 2 ** len(s) and all(max_sum[i] < min_sum[i + 1] for i in range(len(s)))


def answer():
    return sum(sum(s) for s in SETS if is_special(s))


if __name__ == '__main__':
    print("Answer is:", answer())
