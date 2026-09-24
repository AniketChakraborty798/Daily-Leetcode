class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        def digit_sum(n: int) -> int:
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        for i, num in enumerate(nums):
            if digit_sum(num) == i:
                return i
        return -1