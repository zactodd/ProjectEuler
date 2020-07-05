#=
answer009:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem 9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

=#



function answer()
    n = 1000
    for a in 1:n, b in (a + 1):n
        c = n - a - b
        a * a + b * b == c ^ 2 && return a * b * c
    end
    return nothing
end


# Output
println("Answer is: ", answer())
