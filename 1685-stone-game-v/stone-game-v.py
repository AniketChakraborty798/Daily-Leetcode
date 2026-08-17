from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def rangeSum(i, j):
            return prefix[j + 1] - prefix[i]

        dp = [[0] * n for _ in range(n)]
        maxLeft = [[0] * n for _ in range(n)]
        maxRight = [[0] * n for _ in range(n)]

        for i in range(n):
            maxLeft[i][i] = maxRight[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                total = rangeSum(i, j)

                lo, hi, mid = i, j - 1, i - 1
                while lo <= hi:
                    m = (lo + hi) // 2
                    if 2 * rangeSum(i, m) <= total:
                        mid, lo = m, m + 1
                    else:
                        hi = m - 1

                best = 0
                if mid >= i:
                    best = max(best, maxLeft[i][mid])
                    if 2 * rangeSum(i, mid) == total:
                        best = max(best, rangeSum(i, mid) + dp[mid + 1][j])
                if mid + 2 <= j:
                    best = max(best, maxRight[mid + 2][j])

                dp[i][j] = best
                maxLeft[i][j] = max(maxLeft[i][j - 1], dp[i][j] + total)
                maxRight[i][j] = max(maxRight[i + 1][j], dp[i][j] + total)

        return dp[0][n - 1]