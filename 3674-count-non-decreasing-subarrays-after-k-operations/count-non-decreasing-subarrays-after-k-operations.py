from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque()      # prefix-max record indices of window [l..r]
        cost = 0
        r = n - 1
        ans = 0

        for l in range(n - 1, -1, -1):
            # add nums[l] on the left
            while dq and nums[dq[0]] <= nums[l]:
                j = dq.popleft()
                nxt = dq[0] if dq else r + 1
                cost += (nums[l] - nums[j]) * (nxt - j)
            dq.appendleft(l)

            # shrink from the right until affordable
            while cost > k:
                cost -= nums[dq[-1]] - nums[r]
                if dq[-1] == r:
                    dq.pop()
                r -= 1

            ans += r - l + 1

        return ans