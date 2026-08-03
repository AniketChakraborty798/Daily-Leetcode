class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        l = []
        nums.sort()
        n = len(nums)
        
        for k in range(n - 2):
            # Skip duplicate values for k
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            # Optimization: if smallest remaining value > 0, no triplet possible
            if nums[k] > 0:
                break
            
            i, j = k + 1, n - 1
            while i < j:
                total = nums[k] + nums[i] + nums[j]
                if total < 0:
                    i += 1
                elif total > 0:
                    j -= 1
                else:
                    l.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    # Skip duplicates for i and j
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        
        return l