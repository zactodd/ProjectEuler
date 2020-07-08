#=
answer049:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-08

Problem 49:
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

=#
include("../utils.jl")


function is_stepping_prime_perm(n, s)
    a, b = n + s, n + 2 * s
    return Utils.is_prime(n) && Utils.is_prime(a) && Utils.is_prime(b) &&
                Utils.is_perm(n, a) && Utils.is_perm(n, b)
end


function answer()
    n, s = 1487, 3330
    for c in Iterators.cycle([2, 4])
        n += c
        is_stepping_prime_perm(n, s) && return string(n) * string(n + s) * string(n + s * 2)
    end
end


# Output
println("Answer is: ", answer())
