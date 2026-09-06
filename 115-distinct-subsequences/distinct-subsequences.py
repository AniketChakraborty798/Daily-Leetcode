class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if m > n:
            return 0
        
        # dp[j] = number of ways to form t[0:j] using s processed so far
        dp = [0] * (m + 1)
        dp[0] = 1  # empty t always matches (one way)
        
        for i in range(1, n + 1):
            # iterate j from high to low so dp[j-1] is still the "previous row" value
            for j in range(min(i, m), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                # else dp[j] stays the same (equivalent to dp[i-1][j])
        
        return dp[m]