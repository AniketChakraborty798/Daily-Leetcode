from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        M = 1024

        # dp[i][j][x] is True if XOR value x is reachable at (i, j)
        dp = [[[False] * M for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]] = True

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                v = grid[i][j]
                cur = dp[i][j]
                if i > 0:
                    up = dp[i - 1][j]
                    for x in range(M):
                        if up[x]:
                            cur[x ^ v] = True
                if j > 0:
                    left = dp[i][j - 1]
                    for x in range(M):
                        if left[x]:
                            cur[x ^ v] = True

        end = dp[m - 1][n - 1]
        for x in range(M):
            if end[x]:
                return x
        return -1