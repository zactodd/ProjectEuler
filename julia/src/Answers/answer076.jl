#=
answer076:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-11

Problem 76:

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

=#


function answer()
    t = 101
    ways = vcat([1], zeros(t))
    for n in 1:t, i in n:t
        ways[i] += ways[i - n]
    end
    return ways[t]
end


# Output
println("Answer is: ", answer())
