class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 == 1 or grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        dp = [0] * n  # dp[j]: bitset of reachable balances at current row, column j
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    cur = 1  # balance 0 before processing the first cell
                else:
                    cur = dp[j] if i > 0 else 0        # from top
                    if j > 0:
                        cur |= dp[j - 1]               # from left
                if grid[i][j] == '(':
                    cur <<= 1
                else:
                    cur >>= 1
                dp[j] = cur
        return dp[n - 1] & 1 == 1