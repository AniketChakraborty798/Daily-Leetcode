class Solution(object):
    def maxProduct(self, n):
        digits = [int(d) for d in str(n)]
        digits.sort()
        return digits[-1] * digits[-2]