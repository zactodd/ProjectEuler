"""
Problem 178:
Consider the number
.
It can be seen that each pair of consecutive digits of
 has a difference of one.
A number for which every pair of consecutive digits has a difference of one is called a step number.
A pandigital number contains every decimal digit from
 to
 at least once.
How many pandigital step numbers less than
 are there?
"""

import functools


def answer():
	LIMIT = 40
	return sum(pandigital_steps(digits, head, 0, 9) for digits in range(LIMIT + 1) for head in range(1, 10))

@functools.cache
def pandigital_steps(digits, head, low, high):
	if digits <= 1:
		return 1 if (low == head == high) else 0
	else:
		result = 0
		if head - 1 >= low:
			result += pandigital_steps(digits - 1, head - 1, low, high)
			if head == high:
				result += pandigital_steps(digits - 1, head - 1, low, high - 1)
		if head + 1 <= high:
			result += pandigital_steps(digits - 1, head + 1, low, high)
			if head == low:
				result += pandigital_steps(digits - 1, head + 1, low + 1, high)
		assert 0 <= result < 10 ** digits
		return result


if __name__ == '__main__':
	print("Answer is:", answer())
