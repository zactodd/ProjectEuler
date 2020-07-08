#=
answer062:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-08

Problem 62:
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

=#
using DataStructures


function answer()
    ds = []
    d = 5
    cubes = DataStructures.DefaultDict(() -> [])
    for n in Iterators.countfrom(100)
        c::BigInt = n ^ 3
        ds = sort(digits(c))
        append!(cubes[ds], c)
        length(cubes[ds]) == d && return cubes[ds][1]
    end
    return min_cube
end


# Output
println("Answer is: ", answer())


