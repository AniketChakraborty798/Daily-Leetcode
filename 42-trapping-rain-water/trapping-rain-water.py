from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        if n < 1:
            return 0

        ans = 0

        left_max = [0] * n
        right_max = [0] * n

        # Fill left_max array
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # Fill right_max array
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # Calculate trapped water
        for i in range(n):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans