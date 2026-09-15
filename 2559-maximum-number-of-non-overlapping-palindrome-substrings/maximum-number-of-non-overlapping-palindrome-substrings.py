class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0

        # isPal[i][j]: True if s[i..j] is a palindrome
        isPal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    isPal[i][j] = True
                elif s[i] == s[j]:
                    if j - i == 1 or isPal[i + 1][j - 1]:
                        isPal[i][j] = True
                # else stays False

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]  # option: don't end a substring at i-1
            for L in (k, k + 1):
                if L > i:
                    continue
                start = i - L
                if isPal[start][i - 1]:
                    dp[i] = max(dp[i], dp[start] + 1)

        return dp[n]