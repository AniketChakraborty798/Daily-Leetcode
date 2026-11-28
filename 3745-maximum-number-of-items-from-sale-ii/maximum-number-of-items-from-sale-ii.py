from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        cnt = [0] * (n + 1)
        for f, p in items:
            cnt[f] += 1

        # multiples[f] = number of items whose factor is a multiple of f
        multiples = [0] * (n + 1)
        for f in range(1, n + 1):
            s = 0
            for m in range(f, n + 1, f):
                s += cnt[m]
            multiples[f] = s

        pm = min(p for _, p in items)

        cand = []
        for f, p in items:
            d = multiples[f] - 1          # exclude itself
            if d > 0 and p < 2 * pm:
                cand.append((p, d))
        cand.sort()

        R = budget
        ans = 0
        for p, d in cand:
            k = min(d, R // p)
            R -= k * p
            ans += 2 * k
            if k < d:                     # can't afford more of anything pricier
                break

        ans += R // pm
        return ans