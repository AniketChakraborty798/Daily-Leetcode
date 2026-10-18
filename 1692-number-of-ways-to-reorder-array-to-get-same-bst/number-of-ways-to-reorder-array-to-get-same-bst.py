from math import comb
from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        # Precompute Pascal's triangle mod p (n <= 1000)
        n = len(nums)
        C = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            C[i][0] = 1
            for j in range(1, i + 1):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        def dfs(arr: List[int]) -> int:
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            return (C[len(arr) - 1][len(left)] * dfs(left) % MOD) * dfs(right) % MOD

        return (dfs(nums) - 1) % MOD