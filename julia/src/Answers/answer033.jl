#=
answer033:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-05

Problem 33:

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

=#

divmod(a, b) = (div(a, b), a % b)


function answer()
    f = 1
    for i in 1:9, j in 1:i
        q, r = divmod(9 * j * i, 10 * j - i)
        if r == 0 && q <= 9
            f *= i / j
        end
    end
    return floor(f)
end


# Output
println("Answer is: ", answer())
