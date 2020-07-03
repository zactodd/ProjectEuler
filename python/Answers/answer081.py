"""
Problem 81:
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

MATRIX_FILE = "../../resources/matrix.txt"
with open(MATRIX_FILE, "r") as f:
    MATRIX = [list(map(int, row.split(','))) for row in f.readlines()]


def answer():
    matrix = MATRIX.copy()
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1]) if i * j > 0 else \
                (matrix[i - 1][j] if i else (matrix[i][j - 1] if j else 0))
    return matrix[-1][-1]


if __name__ == '__main__':
    print("Answer is:", answer())