"""
Problem 175:

A fraction $p/q$ (reduced to lowest terms) is such that for a certain integer $n > 0$, $f(n)/f(n-1) = p/q$.
$f(0)=1$ and $f(n)$ is the number of ways to express $n$ as a sum of powers of 2, where no power of 2 can appear more than twice.
For example, $f(10) = 5$ because $10 = 8+2 = 8+1+1 = 4+4+2 = 4+2+2+1+1 = 4+4+1+1$.
It can be shown that for any fraction $p/q$ ($p>0, q>0$) in lowest terms there is always an integer $n$ such that $f(n)/f(n-1) = p/q$.
For example, the smallest $n$ for which $f(n)/f(n-1) = 13/17$ is $n=241$.
The binary expansion of $241$ is $11110001$.
The "Shortened Binary Expansion" of $241$ is obtained by counting consecutive ones and zeroes from most significant to least significant bit: $4,3,1$ (4 ones, 3 zeroes, 1 one).

Find the Shortened Binary Expansion of the smallest $n$ for which $f(n)/f(n-1) = 123456789 / 987654321$.
Give the answer as a comma separated string of integers without any whitespaces.
"""
import math
from itertools import takewhile
from python.utils import iterate

def answer():
    p0, q0 = 123456789, 987654321
    cd = math.gcd(p0, q0)
    p, q = p0 // cd, q0 // cd

    coeffs = []
    while p != 0:
        quotient = q // p
        coeffs.append(quotient)
        q, p = p, q % p

    if (len(coeffs) % 2 != 0) != (p / q < 1):
        if coeffs[-1] == 1:
            coeffs.pop() # Remove the 1
            coeffs[-1] += 1 # Increment the new last term
        else:
            coeffs[-1] -= 1
            coeffs.append(1)
    return ",".join(map(str, reversed(coeffs)))

if __name__ == '__main__':
    print("Answer is:", answer())
