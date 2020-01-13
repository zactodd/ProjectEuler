"""
Question 82:
NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.
Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

MATRIX_FILE = "../resources/matrix.txt"
with open(MATRIX_FILE, "r") as f:
    MATRIX = [list(map(int, row.split(','))) for row in f.readlines()]


def answer():
    matrix = MATRIX.copy()
    n, m = len(matrix), len(matrix[0])
    cost = [matrix[i][-1] for i in range(n)]

    for i in range(m - 2, -1, -1):
        cost[0] += matrix[0][i]
        for j in range(1, n):
            cost[j] = min(cost[j], cost[j - 1]) + matrix[j][i]
        for j in range(n - 2, -1, -1):
            cost[j] = min(cost[j], cost[j + 1] + matrix[j][i])
    return min(cost)


if __name__ == '__main__':
    print("Answer is:", answer())
