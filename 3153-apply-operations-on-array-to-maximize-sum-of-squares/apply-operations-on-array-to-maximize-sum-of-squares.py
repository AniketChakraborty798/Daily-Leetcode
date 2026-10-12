class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 30
        for x in nums:
            for b in range(30):
                if (x >> b) & 1:
                    cnt[b] += 1

        ans = 0
        for _ in range(k):
            num = 0
            for b in range(30):
                if cnt[b] > 0:
                    num |= (1 << b)
                    cnt[b] -= 1
            if num == 0:
                break
            ans = (ans + num * num) % MOD
        return ans