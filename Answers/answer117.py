"""
Question 117:
Using a combination of grey square tiles and oblong tiles chosen from: red tiles (measuring two units), green tiles (measuring three units), and blue tiles (measuring four units), it is possible to tile a row measuring five units in length in exactly fifteen different ways.

png117.png
How many ways can a row measuring fifty units in length be tiled?

NOTE: This is related to Problem 116.
"""
from utils import lambda_feedback


def answer():
    n = 50
    inputs = 0, 0, 0, 1
    return lambda_feedback(inputs, lambda x: (x[1], x[2], x[3], sum(x)), n)[-1]


if __name__ == '__main__':
    print("Answer is:", answer())


