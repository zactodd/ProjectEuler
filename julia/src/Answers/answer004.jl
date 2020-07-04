#=
answer004:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem 4:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

=#
include("../utils.jl")


answer() = maximum([i * j for i in 100:999, j in 100:999 if Utils.is_palindrome(i * j)])


# Output
println("Answer is: ", answer())
