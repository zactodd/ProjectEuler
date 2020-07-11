#=
answer106:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-11

Problem 106:
Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
For this problem we shall assume that a given set contains n strictly increasing elements and it already satisfies the second rule.

Surprisingly, out of the 25 possible subset pairs that can be obtained from a set for which n = 4, only 1 of these pairs need to be tested for equality (first rule). Similarly, when n = 7, only 70 out of the 966 subset pairs need to be tested.

For n = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?

NOTE: This problem is related to Problem 103 and Problem 105.

=#




catalan(n) = div(binomial(n * 2, n), n + 1)
answer(s=BigInt(12)) = sum(
    map(i -> binomial(s, i * 2) * (div(binomial(i * 2, i), 2) - catalan(i)), 2:div(s, 2))
)


# Output
println("Answer is: ", answer())
