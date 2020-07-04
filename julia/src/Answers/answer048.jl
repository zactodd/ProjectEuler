#=
answer048:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05
Problem 48:
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

=#


answer(d=10, n=1000) = string(sum([BigInt(i) ^ i for i in 1:n]))[(end - d + 1):end]

# Output
println("Answer is: ", answer())
