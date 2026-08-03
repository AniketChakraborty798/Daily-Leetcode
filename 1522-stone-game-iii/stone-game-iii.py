class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        # dp[i] = best score difference (current player - opponent) from index i onward
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            best = float('-inf')
            total = 0
            # try taking 1, 2, or 3 stones starting at i
            for k in range(1, 4):
                if i + k - 1 < n:
                    total += stoneValue[i + k - 1]
                    best = max(best, total - dp[i + k])
            dp[i] = best
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"