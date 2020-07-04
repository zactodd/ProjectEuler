#=
answer063:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem63:
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

=#

answer(l=25) = sum([length(digits(BigInt(i) ^ j)) == j for i in 1:9, j in 1:(l - 1)])


# Output
println("Answer is: ", answer())
