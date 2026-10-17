class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        # order[i] = original index of the element that should end up at position i
        order = sorted(range(n), key=lambda i: (digit_sum(nums[i]), nums[i]))

        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i] or order[i] == i:
                continue
            # walk the cycle starting at i
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = order[j]
                cycle_len += 1
            swaps += cycle_len - 1
        return swaps