class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # divisors[len] = proper divisors d (1 <= d < len) of len
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)

        # cost[i][j]: min changes to make s[i..j] a semi-palindrome
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = INF
                for d in divisors[length]:
                    m = length // d      # size of each group
                    changes = 0
                    for g in range(d):
                        lo = i + g                   # first element of group
                        hi = i + g + (m - 1) * d     # last element of group
                        while lo < hi:
                            if s[lo] != s[hi]:
                                changes += 1
                            lo += d
                            hi -= d
                    best = min(best, changes)
                cost[i][j] = best

        # dp[p][j]: min cost to split first j chars into p parts
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for j in range(2 * p, n + 1):
                for i in range(2 * (p - 1), j - 1):   # last part s[i..j-1], length >= 2
                    if dp[p - 1][i] < INF:
                        dp[p][j] = min(dp[p][j], dp[p - 1][i] + cost[i][j - 1])

        return dp[k][n]