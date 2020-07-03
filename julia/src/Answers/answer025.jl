#=
answer025:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-03
=#
include("utils.jl")


answer(n=1000) = ceil((log10(5) / 2 + n - 1) / log10(Utils.PHI))


# Output
println("Answer is: ", answer())
