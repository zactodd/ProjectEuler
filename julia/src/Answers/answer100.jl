#=
answer100:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-08

Problem 100:
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.

=#


function answer()
    a::BigInt, b::BigInt, l::BigInt = 3, 4, 10 ^ 12
    while b <= l
        a, b = 3 * a + 2 * b - 2, 4 * a + 3 * b - 3
    end
    return a
end


# Output
println("Answer is: ", answer())
