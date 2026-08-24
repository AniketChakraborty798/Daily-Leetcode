class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]
        
        # M represents dp[i] for decreasing i, starting from i = n (base case dp[n]=0)
        M = prefix[n]  # this is prefix[n] - dp[n], dp[n] = 0
        
        for i in range(n - 1, 1, -1):
            # Before this line, M == dp[i] (max over j > i of prefix[j]-dp[j])
            # Update M to include j = i as a candidate for smaller i's
            M = max(M, prefix[i] - M)
        
        return M