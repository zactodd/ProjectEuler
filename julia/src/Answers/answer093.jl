#=
answer093:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-09

Problem 93:
By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.

=#
using Combinatorics, IterTools


OPS = [(a, b) -> (a + b), (a, b) -> (a * b), (a, b) -> (a - b), (a, b) -> a / b]


function seq_length(s, c=1)
    while c in s
        c += 1
    end
    return c - 1
end


function answer()
    max_n, max_m = 0, 0
    for term in Combinatorics.combinations(1:9, 4)
        s = Set()
        for p in Combinatorics.permutations(term), o in Iterators.product(ntuple(i-> OPS, 3)...)
            x = o[1](o[2](p[1], p[2]), o[3](p[3], p[4]))
            if x % 1 == 0 && x > 0
                union!(s, floor(x))
            end
            x = o[1](o[2](o[3](p[1], p[2]), p[3]), p[4])
            if x % 1 == 0 && x > 0
                union!(s, floor(x))
            end
        end
        s_len = seq_length(s)
        if s_len > max_m
            max_m, max_n = s_len, term
        end
    end
    return join(map(string, max_n))
end


# Output
println("Answer is: ", answer())
