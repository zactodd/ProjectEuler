#=
utils:
- Julia version: 1.4.2
- Author: Zac
- Date: 2020-07-03
=#
module Utils

export gauss

gauss(n) = div(n * (n + 1), 2)

end