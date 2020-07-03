#=
answer001:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-03

Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
=#
include("utils.jl")


divideGauss(n, d) = d * Utils.gauss(div(n, d))
answer(n=999) = divideGauss(n, 5) + divideGauss(n, 3) - divideGauss(n, 15)


# Output
println("Answer is: ", answer())
