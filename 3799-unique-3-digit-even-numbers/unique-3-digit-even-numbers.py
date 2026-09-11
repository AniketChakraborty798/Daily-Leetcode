from itertools import permutations

class Solution:
    def totalNumbers(self, digits):
        seen = set()
        for perm in permutations(digits, 3):
            if perm[0] != 0 and perm[2] % 2 == 0:
                seen.add(perm)
        return len(seen)