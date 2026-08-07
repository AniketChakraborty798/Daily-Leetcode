class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxprof = 0
        for p in prices:

            maxprof = max(maxprof,(p-minp))
            minp = min(minp,p)
    
        return maxprof