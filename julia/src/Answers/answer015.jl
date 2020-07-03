#=
answer015:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-04

Problem 15:
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
=#


answer(n=40, k=20) = binomial(n, k)

# Output
println("Answer is: ", answer())
