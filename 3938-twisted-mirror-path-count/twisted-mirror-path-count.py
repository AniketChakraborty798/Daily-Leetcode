class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        R = [[0] * n for _ in range(m)]
        D = [[0] * n for _ in range(m)]
        R[0][0] = 1

        for i in range(m):
            for j in range(n):
                r, d = R[i][j], D[i][j]
                if r == 0 and d == 0:
                    continue
                if grid[i][j] == 0:
                    t = (r + d) % MOD
                    if j + 1 < n:
                        R[i][j + 1] = (R[i][j + 1] + t) % MOD
                    if i + 1 < m:
                        D[i + 1][j] = (D[i + 1][j] + t) % MOD
                else:
                    if r and i + 1 < m:
                        D[i + 1][j] = (D[i + 1][j] + r) % MOD
                    if d and j + 1 < n:
                        R[i][j + 1] = (R[i][j + 1] + d) % MOD

        return (R[m - 1][n - 1] + D[m - 1][n - 1]) % MOD