#=
answer116:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05
=#


function f(m, n)
    ways = vcat(ones(m), zeros(n - m + 1))
    for i in m:n
        ways[i] += ways[i - 1] + ways[i - m]
    end
    return ways[n] - 1
end


answer(n=50) = f(2, n) + f(3, n) + f(4, n)


# Output
println("Answer is: ", answer())
