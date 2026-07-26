class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        n = len(nums)
        # Option 1: three largest numbers
        option1 = nums[n-1] * nums[n-2] * nums[n-3]
        # Option 2: two smallest (could be negative) * largest
        option2 = nums[0] * nums[1] * nums[n-1]
        return max(option1, option2)