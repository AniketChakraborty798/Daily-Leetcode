class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        for x in nums:
            total ^= x
        if total != 0:
            return n
        # total XOR is 0
        if any(x != 0 for x in nums):
            return n - 1
        return 0