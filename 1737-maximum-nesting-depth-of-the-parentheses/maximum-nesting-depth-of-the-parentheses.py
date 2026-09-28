class Solution:
    def maxDepth(self, s: str) -> int:
        depth = best = 0
        for ch in s:
            if ch == '(':
                depth += 1
                best = max(best, depth)
            elif ch == ')':
                depth -= 1
        return best