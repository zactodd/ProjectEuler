#=
answer047:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-06

Problem 47:

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?


=#

function answer()
    l, n = 10000000, 4
    l += n
    fs = zeros(l)
    c = 0
    for i in 2:l
        if fs[i] == n
            c += 1
            c == n && return i - n + 1
            continue
        end
        c = 0
        if fs[i] == 0
            fs[i:i:end] = map(x -> x + 1, fs[i:i:end])
        end
    end
    return n
end


# Output
println("Answer is: ", answer())


