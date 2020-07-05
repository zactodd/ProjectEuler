#=
answer047:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-06
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


