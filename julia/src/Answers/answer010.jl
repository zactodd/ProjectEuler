#=
answer010:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

=#

include("../utils.jl")


answer(l=2000000) = sum(Utils.sieves(l))

# Output
println("Answer is: ", answer())
