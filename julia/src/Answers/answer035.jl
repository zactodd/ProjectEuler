#=
answer035:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem 35:

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

=#

include("../utils.jl")


circle(n) = map(x -> parse(Int, string(n)[x:end] * string(n)[1:x-1]), 1:length(digits(n)))
function answer()
     n = 1000000
     primes = Utils.sieves(n)
     return sum([all(c in primes for c in circle(p)) for p in primes])
end


# Output
println("Answer is: ", answer())
