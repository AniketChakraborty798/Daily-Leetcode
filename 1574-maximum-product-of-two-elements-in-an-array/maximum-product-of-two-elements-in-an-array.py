class Solution(object):
    def maxProduct(self, nums):
        # find the two largest numbers in one pass
        first = second = float('-inf')
        for n in nums:
            if n > first:
                first, second = n, first
            elif n > second:
                second = n
        return (first - 1) * (second - 1)