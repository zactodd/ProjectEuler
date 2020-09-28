#=
answer147:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-09-10

Problem 147:
In a 3x2 cross-hatched grid, a total of 37 different rectangles could be situated within that grid as indicated in the sketch.


There are 5 grids smaller than 3x2, vertical and horizontal dimensions being important, i.e. 1x1, 2x1, 3x1, 1x2 and 2x2. If each of them is cross-hatched, the following number of different rectangles could be situated within those smaller grids:

1x1	1
2x1	4
3x1	8
1x2	4
2x2	18
Adding those to the 37 of the 3x2 grid, a total of 72 different rectangles could be situated within 3x2 and smaller grids.

How many different rectangles could be situated within 47x43 and smaller grids?
=#


function rect(m, n)
    if m < n
        m, n = n, m
    end
    return div(m * (m + 1) * n * (n + 1), 4) + div(n * ((2 * m - n) * (4 * n ^ 2 - 1) - 3), 6)
end


answer(w=47, h=43) = sum(rect(m, n) for m in 1:w, n in 1:h)


# Output
println("Answer is: ", answer())

