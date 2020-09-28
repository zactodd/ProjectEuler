#=
answer117:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-09-10

Problem 117:
Using a combination of grey square tiles and oblong tiles chosen from: red tiles (measuring two units), green tiles (measuring three units), and blue tiles (measuring four units), it is possible to tile a row measuring five units in length in exactly fifteen different ways.

png117.png
How many ways can a row measuring fifty units in length be tiled?

NOTE: This is related to Problem 116.
=#


answer(n=50) = reduce((x, y) -> [x[2], x[3], x[4], sum(x)], 1:n, init=[0, 0, 0, 1])[3]


# Output
println("Answer is: ", answer())
