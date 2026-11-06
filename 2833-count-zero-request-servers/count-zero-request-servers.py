from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda l: l[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])

        cnt = [0] * (n + 1)
        distinct = 0
        left = right = 0
        m = len(logs)
        ans = [0] * len(queries)

        for i in order:
            q = queries[i]

            # add logs with time <= q
            while right < m and logs[right][1] <= q:
                sid = logs[right][0]
                if cnt[sid] == 0:
                    distinct += 1
                cnt[sid] += 1
                right += 1

            # remove logs with time < q - x
            while left < right and logs[left][1] < q - x:
                sid = logs[left][0]
                cnt[sid] -= 1
                if cnt[sid] == 0:
                    distinct -= 1
                left += 1

            ans[i] = n - distinct

        return ans