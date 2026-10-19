class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less = equal = 0
        for x in nums:
            if x < target:
                less += 1
            elif x == target:
                equal += 1
        return list(range(less, less + equal))