#=
answer056:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem 56:
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
=#


answer() = maximum([sum(map(Int, digits(BigInt(a) ^ b))) for a in 1:99, b in 1:99])


# Output
println("Answer is: ", answer())
