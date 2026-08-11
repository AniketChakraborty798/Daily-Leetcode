class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        need = [0] * 26
        window = [0] * 26

        for ch in s1:
            need[ord(ch) - ord('a')] += 1

        left = 0
        for right in range(m):
            # expand window by including s2[right]
            window[ord(s2[right]) - ord('a')] += 1

            # shrink window from left if it's larger than len(s1)
            if right - left + 1 > n:
                window[ord(s2[left]) - ord('a')] -= 1
                left += 1

            # check match once window size equals n
            if right - left + 1 == n and window == need:
                return True

        return False