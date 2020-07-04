#=
answer016:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem 16:
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

=#

answer(p=1000) = sum(digits(BigInt(2) ^ p))

# Output
println("Answer is: ", answer())
