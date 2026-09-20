class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            letter_value = 26 - (ord(s[i]) - ord('a'))
            position = i + 1
            total += letter_value * position
        return total