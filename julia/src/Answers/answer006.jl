#=
answer006:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-03
=#

include("../utils.jl")


gauss_sqaures(n) = (2 * n + 1) * Utils.gauss(n) / 3
answer(n=100) = Utils.gauss(n) ^ 2 - gauss_sqaures(n)

# Output
println("Answer is: ", answer())
