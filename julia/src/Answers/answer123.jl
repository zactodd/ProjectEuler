#=
answer123:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-10

Problem 123:
Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)n + (pn+1)n is divided by pn2.

For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 109 is 7037.

Find the least value of n for which the remainder first exceeds 10^10.
=#
include("../utils.jl")


function answer()
    l::BigInt = 10 ^ 10
    primes = vcat([0], Utils.sieves(250000))
    for n in 1:2:length(primes)
        2 * n * primes[n] > l && return n
    end
end


# Output
println("Answer is: ", answer())
