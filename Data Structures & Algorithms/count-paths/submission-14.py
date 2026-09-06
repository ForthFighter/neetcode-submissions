class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        import numpy as np

        grid = np.zeros((m,n))

        for i in range(m):
            grid[i][0] = 1

        for j in range(n):
            grid[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return int(grid[m-1][n-1])
        