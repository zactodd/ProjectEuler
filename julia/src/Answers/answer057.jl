#=
answer057:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem 57:
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

2–√=1+1/2+1/2+1/2+…
By expanding this for the first four iterations, we get:

1+1/2=3/2=1.5
1+1/2+1/2=7/5=1.4
1+1/2+1/2+1/2=17/12=1.41666…
1+1/2+1/2+1/2+1/2=41/29=1.41379…

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

=#


function answer()
    n::BigInt, d::BigInt, c = 3, 2, 0
    for _ in 1:1000
        n, d = 2 * d + n, n + d
        if length(string(n)) > length(string(d))
            c += 1
        end
    end
    return c
end


# Output
println("Answer is: ", answer())
