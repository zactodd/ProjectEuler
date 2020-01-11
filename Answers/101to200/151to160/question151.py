"""
Question 151:
A printing shop runs 16 batches (jobs) every week and each batch requires a sheet of special colour-proofing paper of size A5.

Every Monday morning, the foreman opens a new envelope, containing a large sheet of the special paper with size A1.

He proceeds to cut it in half, thus getting two sheets of size A2. Then he cuts one of them in half to get two sheets of size A3 and so on until he obtains the A5-size sheet needed for the first batch of the week.

All the unused sheets are placed back in the envelope.


At the beginning of each subsequent batch, he takes from the envelope one sheet of paper at random. If it is of size A5, he uses it. If it is larger, he repeats the 'cut-in-half' procedure until he has what he needs and any remaining sheets are always placed back in the envelope.

Excluding the first and last batch of the week, find the expected number of times (during each week) that the foreman finds a single sheet of paper in the envelope.

Give your answer rounded to six decimal places using the format x.xxxxxx .
"""


def remove(cnt, i):
    ret = cnt[:]
    ret[i] -= 1
    for j in range(i + 1, 5):
        ret[j] += 1
    return ret


def answer():
    f = {}

    def recur(dep, cnt):
        if dep == 0:
            return 0
        state = tuple(cnt)
        if state not in f:
            tot = sum(cnt)
            f[state] = sum(recur(dep - 1, remove(cnt, i)) * cnt[i] / tot for i in range(5) if cnt[i] != 0) + tot == 1
        return f[state]

    return round(recur(16, [1, 0, 0, 0, 0]) - 2, 6)


if __name__ == '__main__':
    print("Answer is:", answer())
