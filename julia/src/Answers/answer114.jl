#=
answer114:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-04

Problem 114:
A row measuring seven units in length has red blocks with a minimum length of three units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one grey square. There are exactly seventeen ways of doing this.

p114.png
How many ways can a row measuring fifty units in length be filled?

NOTE: Although the example above does not lend itself to the possibility, in general it is permitted to mix block sizes. For example, on a row measuring eight units in length you could use red (3), grey (1), and red (4).
=#


function answer()
    m, n = 3, 50
    ways = vcat(ones(m), zeros(n - m + 1))
    for k in (m + 1):(n + 1)
        ways[k] = ways[k - 1] + sum(ways[1:k - m - 1]) + 1
    end
    return ways[n + 1]
end


# Output
println("Answer is: ", answer())

