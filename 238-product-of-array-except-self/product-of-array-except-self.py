class Solution(object):
    def productExceptSelf(self, nums):
        ls = [1]*len(nums)
        rs = [1]*len(nums)
        f = [1]*len(nums)

        for i in range(1, len(nums)):
            ls[i] = ls[i-1] * nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            rs[j] = rs[j+1] * nums[j+1]
        for k in range(len(nums)):
            f[k] = ls[k] * rs[k]

        return f