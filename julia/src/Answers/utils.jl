#=
utils:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-03
=#
module Utils

export gauss, nth_fib

SQRT5 = sqrt(5)
PHI = (1 + SQRT5) / 2

nth_fib(n) = round((PHI ^ n) / SQRT5)
gauss(n) = div(n * (n + 1), 2)


end