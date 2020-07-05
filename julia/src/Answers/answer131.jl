#=
answer131:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem 131:
There are some prime values, p, for which there exists a positive integer, n, such that the expression n3 + n2p is a perfect cube.

For example, when p = 19, 83 + 82×19 = 123.

What is perhaps most surprising is that for each prime with this property the value of n is unique, and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?

=#

include("../utils.jl")

answer(m=BigInt(1000000)) = length(
    intersect(Set(Utils.sieves(m)), Set(map(x -> 3 * x ^ 2 + 3 * x + 1, 1:floor(sqrt(m / 3)))))
)

# Output
println("Answer is: ", answer())

