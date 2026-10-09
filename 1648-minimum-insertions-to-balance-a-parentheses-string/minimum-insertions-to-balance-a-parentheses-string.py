class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0   # insertions made
        need = 0  # ')' still required for currently open '('

        for ch in s:
            if ch == '(':
                if need % 2 == 1:
                    # previous '(' has only one ')' so far; add a ')' to finish it
                    ans += 1
                    need -= 1
                need += 2
            else:  # ch == ')'
                need -= 1
                if need < 0:
                    # no '(' to match: insert one '('
                    ans += 1
                    need = 1  # new '(' needs 2, this ')' supplied 1

        return ans + need