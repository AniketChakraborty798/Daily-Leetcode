class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = []
        for x in s:
            if x.isalnum():
                t.append(x)
        
        i, j = 0, len(t) - 1
        while i <= j:
            if t[i].lower() != t[j].lower():
                return False
            i += 1
            j -= 1
        return True