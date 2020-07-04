#=
answer085:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-04

Problem 85:
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:


Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
=#


function answer()
    limit, x, min_diff = 2000000, 2, Inf
    area = nothing
    for x in Iterators.countfrom(2, 2)
        y = floor(sqrt(limit * 4 / (x * x + x)))
        x > y && return area
        d = abs(div(x * (x + 1) * y * (y + 1), 4) - limit)
        if d < min_diff
            println(x, " ",y)
            area, min_diff, xx, yy = x * y, d, x, y
        end
    end
    return nothing
end


# Output
println("Answer is: ", answer())
