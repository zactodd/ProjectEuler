#=
answer020:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem 20:
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

=#


answer(n=BigInt(100)) = sum(digits(factorial(n)))

# Output
println("Answer is: ", answer())
