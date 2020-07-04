#=
answer053:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem 53:

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (53)=10.

In general, (nr)=n!r!(n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.

It is not until n=23, that a value exceeds one-million: (2310)=1144066.

How many, not necessarily distinct, values of (nr) for 1≤n≤100, are greater than one-million?

=#


answer(l=1000000) = sum([binomial(BigInt(n), BigInt(k)) > l for n in 1:100 for k in 0:n])

# Output
println("Answer is: ", answer())
