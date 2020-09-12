#=
utils:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-03
=#
module Utils

export PHI, SQRT5, SMALL_PRIMES, gauss, nth_fib, is_prime, is_palindrome, sieves, reciprocal_mod

using IterTools, ResumableFunctions

SQRT5 = sqrt(5)
PHI = (1 + SQRT5) / 2

nth_fib(n) = round((PHI ^ n) / SQRT5)
gauss(n) = div(n * (n + 1), 2)
is_palindrome(n::Int) = string(n) == reverse(string(n))
is_palindrome(n::Array) = n == reverse(n)
is_perm(a, b) = sort(digits(a)) == sort(digits(b))
is_coprime(p, i) = !any(x -> i % x == 0, p)

function is_prime(n)
    if n & 1 == 0
        return false
    else
        return all(n % d != 0 for d in 3:2:(sqrt(n) + 1))
    end
end


function nth_prime(n)
    n == 1 && return 2

    primes = [2]
    for num in Iterators.countfrom(3, 2)
        if is_prime(num)
            append!(primes, num)
        end
        length(primes) == n && return num
    end
end


SMALL_PRIMES = vcat([2], [n for n in 3:2:1000 if is_prime(n)])


function sieves(n)
       is_prime = ones(Bool, n)
       is_prime[1] = false
       for i in 2:BigInt(round(sqrt(n)))
           if is_prime[i]
              for j in (i * i):i:n
                is_prime[j] = false
              end
           end
      end
     return filter(x -> is_prime[x], 1:n)
end


function reciprocal_mod(x, m)
    y = x
    x = m
    a, b = 0, 1
    while y != 0
        a, b = b, a - div(x, y) * b
        x, y = y, x % y
    end
    return a % m
end

function totients(n)
    results = Array(1:n)
    for i in 2:n
        if results[i] == i
            results[i:i:n] -= results[i:i:n] / i
        end
    end
    return results
end

end