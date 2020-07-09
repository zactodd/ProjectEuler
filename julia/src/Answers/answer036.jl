#=
answer036:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-09

Problem 36:

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

=#
include("../utils.jl")


answer(n=1000000) = sum(
    map(x -> Utils.is_palindrome(digits(x)) && Utils.is_palindrome(digits(x, base=2)) * x, 1:n - 1)
)


#Output
println("Answer is: ", answer())
