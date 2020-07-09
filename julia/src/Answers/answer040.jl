#=
answer040:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-09

Problem 40:

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

=#


function answer()
    l = 1000000
    c = join(map(string, 1:l))
    return prod(map(i -> parse(Int, c[10 ^ i]), 1:6))
end


# Output
println("Answer is: ", answer())
