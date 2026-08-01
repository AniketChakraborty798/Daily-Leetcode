class Solution:
    def predictTheWinner(self, nums):
        n = len(nums)
        if n <= 1:
            return True
        
        dp = nums[:]
        
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                dp[i] = max(nums[i] - dp[i + 1], nums[j] - dp[i])
        
        return dp[0] >= 0