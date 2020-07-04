# ProjectEuler
Each of the problems' answer for problem 1 to problem 150
are included in the languages "Answer" directory. 

## Python
The answers .py files have the follow format:

```python
"""
Problem <Problem Number>:

<Problem Question>
"""
import # if any there are any imports

... # helper code

def answer():
    ... # code
    return # answer here


if __name__ == '__main__':
    print("Answer is:", answer())
```


## Juila
The answer .jl files are in the following format.
```juila
#=
answer<problem number>:
- Julia version: <version>
- Author: <author>
- Date: <date>

Problem <Problem Number>:

<Problem Question>
=#

# One of
answer(...) = ...

function answer(...)
    ...
end

# Output
println("Answer is: ", answer())
