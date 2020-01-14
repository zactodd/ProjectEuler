"""
Problem 122:
The most naive way of computing n15 requires fourteen multiplications:

n × n × ... × n = n15

But using a "binary" method you can compute it in six multiplications:

n × n = n2
n2 × n2 = n4
n4 × n4 = n8
n8 × n4 = n12
n12 × n2 = n14
n14 × n = n15

However it is yet possible to compute it in only five multiplications:

n × n = n2
n2 × n = n3
n3 × n3 = n6
n6 × n6 = n12
n12 × n3 = n15

We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.

For 1 ≤ k ≤ 200, find ∑ m(k).
"""

from itertools import count


def answer():
    limit = 200
    min_ops = [0, 0] + [None] * (limit - 1)
    num_unknown = [limit - 1]

    def chains(chain, max_ops):
        if len(chain) > max_ops or num_unknown[0] == 0:
            return
        max_chain_end = chain[-1]
        for i in range(len(chain) - 1, -1, -1):
            for j in range(i, -1, -1):
                if (x := (chain[i] + chain[j])) <= max_chain_end:
                    break
                elif x <= limit:
                    chain.append(x)
                    if min_ops[x] is None:
                        min_ops[x] = len(chain) - 1
                        num_unknown[0] -= 1
                    chains(chain, max_ops)
                    chain.pop()

    for o in count(1):
        if num_unknown[0] == 0:
            return sum(min_ops)
        else:
            chains([1], o)


if __name__ == '__main__':
    print("Answer is:", answer())
