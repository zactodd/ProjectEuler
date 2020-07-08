#=
answer072:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-08
=#
include("../utils.jl")

answer(l=1000000) = sum(Utils.totients(l)) - 1


# Output
println("Answer is: ", answer())
