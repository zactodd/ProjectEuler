#=
answer046:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem 46:

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

=#

function answer()
    n = 5
    primes = Set()
    for c in Iterators.cycle([2, 4])
        if all(n % p != 0 for p in primes)
            union!(primes, n)
        elseif !any((n - 2 * i ^ 2) in primes for i in 1:(n - 1))
            break
        end
        n += c
    end
    return n
end


# Output
println("Answer is: ", answer())
