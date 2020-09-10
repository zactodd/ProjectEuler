#=
answer173:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-09-10

Problem 173:

We shall define a square lamina to be a square outline with a square "hole" so that the shape possesses vertical and horizontal symmetry. For example, using exactly thirty-two square tiles we can form two different square laminae:


With one-hundred tiles, and not necessarily using all of the tiles at one time, it is possible to form forty-one different square laminae.

Using up to one million tiles how many different square laminae can be formed?
=#


function answer(t=1000000)
    t = div(t, 4)
    return sum(div(t, i) - i for i in 1:sqrt(t))
end


# Output
println("Answer is: ", answer())
