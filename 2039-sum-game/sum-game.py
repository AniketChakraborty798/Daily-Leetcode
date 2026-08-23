class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        first, second = num[:half], num[half:]
        
        a = first.count('?')
        b = second.count('?')
        
        diff0 = sum(int(c) for c in first if c != '?') - sum(int(c) for c in second if c != '?')
        
        q = a + b
        if q % 2 == 1:
            return True  # Alice makes the last move, she always wins
        
        # q is even: Bob's forced result under optimal pairing strategy
        forced_diff = diff0 + 9 * (a - b) // 2
        return forced_diff != 0