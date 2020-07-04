#=
answer034:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem 34:

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

=#


DIGIT_FACT = [factorial(d) for d in 0:9]

answer(l=100000) = sum([i for i in 10:l - 1 if i == sum(DIGIT_FACT[[d + 1 for d in digits(i)]])])

# Output
println("Answer is: ", answer())

