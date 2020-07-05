#=
utils:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-03
=#
module Utils

export PHI, SQRT5, gauss, nth_fib, is_prime, is_palindrome, sieves, reciprocal_mod


SQRT5 = sqrt(5)
PHI = (1 + SQRT5) / 2

nth_fib(n) = round((PHI ^ n) / SQRT5)
gauss(n) = div(n * (n + 1), 2)
is_palindrome(n) = string(n) == reverse(string(n))

function is_prime(n)
    if n & 1 == 0
        return false
    else
        return all(n % d != 0 for d in 3:2:(sqrt(n) + 1))
    end
end


function primes()
    produce(2)
    for n in Iterators.countfrom(3, 2)
        if is_prime(n)
            produce(n)
        end
    end
end


# nth_prime(n) = IterTools.nth(primes, n)

is_coprime(p, i) = !any(x -> i % x == 0, p)

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

end