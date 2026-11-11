class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def f(k):
            return (k * costBoth
                    + max(0, need1 - k) * cost1
                    + max(0, need2 - k) * cost2)

        lo, hi = min(need1, need2), max(need1, need2)
        return min(f(0), f(lo), f(hi))