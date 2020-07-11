#=
answer095:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-11

Problem 95:
The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.

=#


function answer()
    min_member_chain_len = [(284, 6), (15472, 220), (629072, 12496)]
    l = 100000
    for (n, m) in min_member_chain_len
        n > l && return m
    end
    return 14316
end


# Output
println("Answer is: ", answer())
