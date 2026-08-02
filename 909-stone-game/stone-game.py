class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = piles[:]  # dp[i] represents dp[i][i] initially
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i] = max(piles[i] - dp[i+1], piles[j] - dp[i])
        
        return dp[0] > 0