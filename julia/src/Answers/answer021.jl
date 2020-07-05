#=
answer021:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem 21:
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

=#


function divisor_sums(n)
    ds = zeros(n)
    for i in 1:n, j in (i * 2):i:n
        ds[j] += i
    end
    return ds
end


function answer()
    n = 10000
    ds = divisor_sums(n)
    return sum([i for (i, s) in enumerate(ds) if s != i && s < n && ds[Int(s)] == i])
end


# Output
println("Answer is: ", answer())
