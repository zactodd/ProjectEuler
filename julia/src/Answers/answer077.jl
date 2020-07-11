#=
answer077:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-11

Problem 77:

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?

=#

include("../utils.jl")


function answer()
    l = 5000
    for t in Iterators.countfrom(10)
        ways = vcat([1], zeros(t))
        for p in Utils.SMALL_PRIMES, i in p:t
            ways[i] += ways[i - p]
        end
        ways[t] > l && return t - 1
    end
end


# Output
println("Answer is: ", answer())


