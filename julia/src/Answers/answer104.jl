#=
answer104:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-08

Problem 100:
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.

=#
include("../utils.jl")


is_pandigital(n) = Utils.is_perm(n, 123456789)


function top(n)::Int
    t = n * 0.20898764024997873 - 0.3494850021680094
    return floor(BigInt(10) ^ (t - floor(t) + 8))
end


function answer()
    fn, f0, f1 = 2, 1, 1
    while !is_pandigital(f1) || !is_pandigital(top(fn))
        f0, f1 = f1, (f1 + f0) % 10 ^ 9
        fn += 1
    end
    return fn
end


# Output
println("Answer is: ", answer())