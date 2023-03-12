"""
Script:
Author:
Date:

Description:


"""
import numpy as np
import copy

N=50
sqrt = lambda x: x ** (1 / 2)
w = .92
max_iterations = 2500
threshold = 1e-8


def intialize_grid(xmin, xmax, ymin, ymax, N, inner_r, outer_r, phi) -> [[(float, int)]]:
    """


    """

    X = np.linspace(xmin, xmax, 2 * N + 1)
    Y = np.linspace(ymin, ymax, 2 * N + 1)

    grid = []
    ground = 0
    flag = 1
    for y in Y:
        row = []
        for x in X:
            if sqrt(x ** 2 + y ** 2) <= inner_r:
                if sqrt(x ** 2 + y ** 2) == inner_r:
                    row.append((phi, flag))
                else:
                    row.append((phi, flag - 1))
            elif sqrt(x ** 2 + y ** 2) >= inner_r:
                if sqrt(x ** 2 + y ** 2) == outer_r:
                    row.append((ground, flag))
                else:
                    row.append((ground, flag - 1))
        grid.append(row)
    return grid


def overrelax(grid, threshold,w) -> None:
    """

    """

    potential_index = 0
    flag_index = 1
    diff_iteration = 1
    iterator = 0

    while iterator < max_iterations:

        prev_grid = copy.deepcopy(grid)
        diffs = []
        for i in range(0, len(X) - 1):
            for j in range(0, len(Y) - 1):
                if grid[i][j][flag_index] == flag_index:
                    pass
                elif grid[i][j][flag_index] == flag_index - 1:
                    grid[i][j][potential_index] = (1 + w) / 4 * (
                            grid[i + 1][j][potential_index] + grid[i - 1][j][potential_index] + grid[i][j + 1][
                        potential_index] + grid[i][j - 1][potential_index]) - w * grid[i][j][potential_index]
                    diffs.append(grid[i][j][potential_index] - prev_grid[i][j][potential_index])

        if max(diffs) <= threshold:
            break

        iterator += 1


X = np.linspace(-.007, .007, 2 * N + 1)
Y = np.linspace(-.007, .007, 2 * N + 1)

grid = []
flag = 1
for y in Y:
    row = []
    for x in X:
        if sqrt(x ** 2 + y ** 2) <= .001:
            row.append([100, flag])
        elif sqrt(x ** 2 + y ** 2) >= .001:
            if sqrt(x ** 2 + y ** 2) == .007:
                row.append([0, flag])
            else:
                row.append([0, flag - 1])
    grid.append(row)

potential_index = 0
flag_index = 1
diff_iteration = 1
iterator = 0
while iterator < max_iterations:

    prev_grid = copy.deepcopy(grid)
    diffs = []
    for i in range(0, len(X) - 1):
        for j in range(0, len(Y) - 1):
            if grid[i][j][flag_index] == flag_index:
                pass
            elif grid[i][j][flag_index] == flag_index-1:
                grid[i][j][potential_index] = (1 + w) / 4 * (
                            grid[i + 1][j][potential_index] + grid[i - 1][j][potential_index] + grid[i][j + 1][
                        potential_index] + grid[i][j - 1][potential_index]) - w * grid[i][j][potential_index]
                diffs.append(grid[i][j][potential_index] - prev_grid[i][j][potential_index])

    if max(diffs)<=threshold:
        break

    iterator += 1
