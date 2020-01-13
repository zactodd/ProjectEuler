"""
Question 83:
NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.
Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""
import networkx as nx


MATRIX_FILE = "../resources/matrix.txt"
with open(MATRIX_FILE, "r") as f:
    MATRIX = [list(map(int, row.split(','))) for row in f.readlines()]


def answer():
    matrix = MATRIX.copy()
    n, m = len(matrix), len(matrix[0])

    g = nx.DiGraph()
    for i in range(n):
        for j in range(m):
            neighbors = [(i + x, j + y) for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]
                         if 0 <= i + x < n and 0 <= j + y < m]
            for ix, jy in neighbors:
                g.add_edge((i, j), (ix, jy), weight=matrix[ix][jy])
    return nx.dijkstra_path_length(g, source=(0, 0), target=(n - 1, m - 1)) + matrix[0][0]


if __name__ == '__main__':
    print("Answer is:", answer())
