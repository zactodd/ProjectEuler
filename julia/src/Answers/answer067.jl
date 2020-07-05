#=
answer067:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem 67:
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

=#

io = open("../resources/triangle.txt", "r")
TRIANGLE = split(strip(read(io, String)), "\n")
close(io)


TRIANGLE =  [map(x -> parse(Int, x), split(row)) for row in TRIANGLE]


function answer(triangle=TRIANGLE)
    for row in length(triangle):-1:1, col in 1:(row - 1)
        triangle[row - 1][col] += max(triangle[row][col], triangle[row][col + 1])
    end
    return triangle[1][1]
end


# Output
println("Answer is: ", answer())


