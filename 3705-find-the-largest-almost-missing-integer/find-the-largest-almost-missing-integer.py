class Solution:
    def largestInteger(self, nums, k):
        from collections import defaultdict
        n = len(nums)
        count = defaultdict(int)
        for s in range(n - k + 1):
            window = set(nums[s:s+k])
            for x in window:
                count[x] += 1
        ans = -1
        for x, c in count.items():
            if c == 1:
                ans = max(ans, x)
        return ans