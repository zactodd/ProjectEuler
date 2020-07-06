#=
answer019:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-06

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

=#
using Dates


function answer()
    start, finish = Dates.DateTime(1900, 7, 1), Dates.DateTime(2000, 12, 31)
    return sum([Dates.day(t) == 1 for t in start:Dates.Day(7):finish]) - 1
end


# Output
println("Answer is: ", answer())
