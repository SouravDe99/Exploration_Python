import numpy as np

n = 10
m = 3.0 / 2.0
grid = np.zeros((n + 1, n + 1), dtype=int)

for i in range(n + 1):
    for j in range(n + 1):
        if j - m * i > 0:
            grid[i, j] = 0
        elif (i == 0) or (j == 0):
            grid[i, j] = 1
        else:
            grid[i, j] = grid[i - 1, j] + grid[i, j - 1]

print(np.rot90(grid))
