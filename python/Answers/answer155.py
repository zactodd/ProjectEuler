"""
Problem 155:
An electric circuit uses exclusively identical capacitors of the same value C.
The capacitors can be connected in series or in parallel to form sub-units, which can then be connected in series or in parallel with other capacitors or other sub-units to form larger sub-units, and so on up to a final circuit.

Using this simple procedure and up to n identical capacitors, we can make circuits having a range of different total capacitances. For example, using up to n=3 capacitors of 60 F each, we can obtain the following 7 distinct total capacitance values:


If we denote by D(n) the number of distinct total capacitance values we can obtain when using up to n equal-valued capacitors and the simple procedure described above, we have: D(1)=1, D(2)=3, D(3)=7 ...

Find D(18).

Reminder : When connecting capacitors C1, C2 etc in parallel, the total capacitance is CT = C1 + C2 +...,
whereas when connecting them in series, the overall capacitance is given by: $\dfrac{1}{C_T} =\dfrac{1}{C_1} +\dfrac{1}{C_2} + ...$
"""

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


if __name__ == '__main__':
    print("Answer is:", answer())
