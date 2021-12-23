import math


def parallel_series(n0, d0, n1, d1):
    psum, nprod, dprod = n0 * d1 + n1 * d0, n0 * n1, d0 * d1
    npgcd, dpgcd = math.gcd(psum, nprod), math.gcd(psum, dprod)
    return {(psum // dpgcd, dprod // dpgcd), (nprod // npgcd, psum // npgcd)}


def answer(s=18):
    possible = [set(), {(60, 1)}]
    all_possible = {(60, 1)}
    for i in range(2, s + 1):
        possible.append(update := {p for j in range(1, i // 2 + 1) for n1, d1 in possible[i - j]
                                    for n0, d0 in possible[j] for p in parallel_series(n0, d0, n1, d1)})
        all_possible |= update
    return len(all_possible)

