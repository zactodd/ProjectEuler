#=
answer039:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-09-10

Problem 39:

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
=#


py_triple(n) = sum(a * a + b * b == (n - a - b) ^ 2 for a in 1:n + 1 for b in a + 1:n + 1)
answer(n=1000) = argmax(py_triple.(1:n))


# Output
println("Answer is: ", answer())
