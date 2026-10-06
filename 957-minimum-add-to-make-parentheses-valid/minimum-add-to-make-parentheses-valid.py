class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        add = 0
        for ch in s:
            if ch == '(':
                open_count += 1
            elif open_count > 0:
                open_count -= 1
            else:
                add += 1
        return add + open_count