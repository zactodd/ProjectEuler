#=
answer120:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-09-10
=#


answer(l=1000) = sum(i * (i - (i % 2) + 1) for i in 3:l)


# Output
println("Answer is: ", answer())
