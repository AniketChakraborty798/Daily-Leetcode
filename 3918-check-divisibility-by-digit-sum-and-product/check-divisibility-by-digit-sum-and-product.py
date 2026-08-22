class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s, p, x = 0, 1, n
        while x:
            d = x % 10
            s += d
            p *= d
            x //= 10
        return n % (s + p) == 0