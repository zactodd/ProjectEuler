#=
answer104:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-08
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