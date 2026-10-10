from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        m = max(abs(a - b) for a, b in zip(nums1, nums2))
        cnt = [0] * (m + 1)
        for a, b in zip(nums1, nums2):
            cnt[abs(a - b)] += 1

        for v in range(m, 0, -1):
            if k == 0:
                break
            c = cnt[v]
            if c == 0:
                continue
            if c <= k:
                cnt[v - 1] += c
                cnt[v] = 0
                k -= c
            else:
                cnt[v - 1] += k
                cnt[v] = c - k
                k = 0

        return sum(v * v * c for v, c in enumerate(cnt))