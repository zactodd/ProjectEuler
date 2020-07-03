#=
answer006:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-03
=#

include("utils.jl")


gaussSqures(n) = (2 * n + 1) * Utils.gauss(n) / 3
answer(n=100) = Utils.gauss(n) ^ 2 - gaussSqures(n)

# Output
println("Answer is: ", answer())
