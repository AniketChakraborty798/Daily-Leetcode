class Solution(object):
    def reverse(self, x):
        temp = abs(x)
        result = 0
        while temp > 0:
            result = result * 10 + temp % 10
            temp = temp // 10
        if result > (2**31-1) or result < -2**31:
            return 0
        else:
            if x > 0:
                return result
            else:
                return -result