#=
answer024:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-06

Problem 24;
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

=#
using Combinatorics, IterTools


answer(n=BigInt(1000000)) = join(map(string, IterTools.nth(Combinatorics.permutations(0:9, 9), n)))


# Output
println("Answer is: ", answer())
