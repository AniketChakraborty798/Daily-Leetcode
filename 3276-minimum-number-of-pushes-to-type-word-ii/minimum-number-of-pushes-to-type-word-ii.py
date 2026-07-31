from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = sorted(Counter(word).values(), reverse=True)
        total = 0
        for i, f in enumerate(freq):
            total += (i // 8 + 1) * f
        return total