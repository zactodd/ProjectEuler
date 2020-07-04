#=
utils:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-03
=#
module Utils

export PHI, SQRT5, gauss, nth_fib, is_prime, is_palindrome


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

end