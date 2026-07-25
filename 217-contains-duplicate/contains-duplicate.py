class Solution(object):
    def containsDuplicate(self, nums):
        s = set()
        for x in nums:
            if x not in s:
                s.add(x)
            else:
                return True
        return False