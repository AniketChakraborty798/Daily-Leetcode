class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float('inf')
        best = [INF] * n
        ans = INF
        left = 0
        cur_sum = 0

        for right in range(n):
            cur_sum += arr[right]
            while cur_sum > target:
                cur_sum -= arr[left]
                left += 1

            if cur_sum == target:
                length = right - left + 1
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])
                best[right] = min(best[right - 1] if right > 0 else INF, length)
            else:
                best[right] = best[right - 1] if right > 0 else INF

        return ans if ans != INF else -1