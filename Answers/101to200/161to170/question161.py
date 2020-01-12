"""
Question 161:
A triomino is a shape consisting of three squares joined via the edges. There are two basic forms:



If all possible orientations are taken into account there are six:



Any n by m grid for which nxm is divisible by 3 can be tiled with triominoes.
If we consider tilings that can be obtained by reflection or rotation from another tiling as different there are 41 ways a 2 by 9 grid can be tiled with triominoes:



In how many ways can a 9 by 12 grid be tiled in this way by triominoes?
"""


def first_empty_cell(n, grid):
    for i in range(n):
        for j in range(9):
            if not grid[i][j]:
                return i, j
    return None


def place_triomino(n, grid, triomino, empty_cell):
    ex, ey = empty_cell
    for tx, ty in triomino:
        x, y = ex + tx, ey + ty
        if x < 0 or x >= n or y < 0 or y >= 9:
            return None
        elif grid[x][y]:
            return None

    result = [[False for _ in range(9)] for _ in range(n)]
    for i in range(n):
        for j in range(9):
            result[i][j] = grid[i][j]
    for tx, ty in triomino:
        x, y = ex + tx, ey + ty
        result[x][y] = True
    return tuple(tuple(row) for row in result)


def answer():
    n = 12
    triomino_list = [
        [(0, 0), (1, 0), (0, 1)],
        [(0, 0), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (1, -1)],
        [(0, 0), (0, 1), (0, 2)],
        [(0, 0), (1, 0), (2, 0)],
    ]

    start = tuple(tuple(False for _ in range(9)) for _ in range(n))
    end = tuple(tuple(True for _ in range(9)) for _ in range(n))
    ways = [{} for _ in range(3 * n + 1)]
    ways[0][start] = 1
    for i in range(3 * n):
        for top in ways[i]:
            empty_cell = first_empty_cell(n, top)
            for t in triomino_list:
                next_grid = place_triomino(n, top, t, empty_cell)
                if not next_grid:
                    continue
                elif next_grid not in ways[i + 1]:
                    ways[i + 1][next_grid] = 0
                ways[i + 1][next_grid] += ways[i][top]
    return ways[3 * n][end]


if __name__ == '__main__':
    print("Answer is:", answer())


