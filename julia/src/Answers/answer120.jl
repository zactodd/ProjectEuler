#=
answer120:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-09-10

Problem 120:
Let r be the remainder when (a−1)n + (a+1)n is divided by a2.

For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

For 3 ≤ a ≤ 1000, find ∑ rmax.
=#


answer(l=1000) = sum(i * (i - (i % 2) + 1) for i in 3:l)


# Output
println("Answer is: ", answer())
