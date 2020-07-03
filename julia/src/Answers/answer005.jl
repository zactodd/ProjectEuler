#=
answer005:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-03

Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
=#



function answer()
    p = 1
    for i in 1:21
        p *= div(i, gcd(i, p))
    end
    return p
end


# Output
println("Answer is: ", answer())
