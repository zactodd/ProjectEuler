#=
answer046:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05
=#

function answer()
    n = 5
    primes = Set()
    for c in Iterators.cycle([-1, 1])
        if all(n % p != 0 for p in primes)
            union!(primes, n)
        elseif !any((n - 2 * i ^ 2) in primes for i in 1:(n - 1))
            break
        end
        n += 3 + c
    end
    return n
end


# Output
println("Answer is: ", answer())
