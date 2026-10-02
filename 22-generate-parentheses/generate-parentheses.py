class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur, open_cnt, close_cnt):
            if len(cur) == 2 * n:
                res.append("".join(cur))
                return
            if open_cnt < n:
                cur.append("(")
                backtrack(cur, open_cnt + 1, close_cnt)
                cur.pop()
            if close_cnt < open_cnt:
                cur.append(")")
                backtrack(cur, open_cnt, close_cnt + 1)
                cur.pop()

        backtrack([], 0, 0)
        return res