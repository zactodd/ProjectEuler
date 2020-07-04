#=
answer031:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem 31:

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

=#


COINS = [1, 2, 5, 10, 20, 50, 100, 200]

function answer()
    t = 200
    ways = vcat([1], zeros(t))
    for c in COINS, i in c:(t + 1)
        ways[i] += ways[i - c]
    end
    return ways[t + 1]
end


# Output
println("Answer is: ", answer())
