from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        INF = float('inf')
        ans = INF
        k = nums[0]

        # Case A: rotation of increasing array
        if all(nums[i] == (i + k) % n for i in range(n)):
            if k == 0:
                ans = 0
            else:
                ans = min(n - k, k + 2)

        # Case B: rotation of decreasing array
        if all(nums[i] == (k - i) % n for i in range(n)):
            kp = (k + 1) % n
            ans = min(ans, kp + 1, 1 + (n - kp) % n)

        return -1 if ans == INF else ans