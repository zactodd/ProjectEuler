#=
answer007:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-09

Problem 7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

=#
include("../utils.jl")


answer(n=10001) = Utils.nth_prime(n)


# Output
println("Answer is: ", answer())
