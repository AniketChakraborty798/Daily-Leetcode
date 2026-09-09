class Solution:
    def countCommas(self, n: int) -> int:
        s = str(n)
        D = len(s)
        total = 0
        
        # Complete groups: digit-lengths 1 .. D-1
        for d in range(1, D):
            count = 9 * (10 ** (d - 1))   # numbers with exactly d digits
            commas_per_num = (d - 1) // 3
            total += count * commas_per_num
        
        # Final (partial) group: digit-length D, from 10^(D-1) to n
        count_last = n - 10 ** (D - 1) + 1
        commas_last = (D - 1) // 3
        total += count_last * commas_last
        
        return total
