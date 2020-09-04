"""
Problem 17:
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

Solved: O(n)
"""


def numbers_to_word_length(n):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousand = ["", "Thousand"]
    words = []
    number = map(''.join, zip(*[iter(str(n).zfill(18))]*3))
    for nx, g in enumerate(number, 1):
        if g == "000":
            continue
        h, t, o = map(int, g)
        if h > 0:
            words += [ones[h], "Hundred"]
        if t == 1:
            words += [teens[o]] if o > 0 else [tens[t]]
        else:
            if t > 0:
                words += [tens[t]]
            if o > 0:
                words += [ones[o]]
        words += [thousand[6 - nx]]
    return len("".join(words)) + 3 * ("Hundred" in words and "Hundred" != words[-2])


def answer(n=1000):
    return sum(numbers_to_word_length(i) for i in range(1, n + 1))


if __name__ == '__main__':
    print("Answer is:", answer())
