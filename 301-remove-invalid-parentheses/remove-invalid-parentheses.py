class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Count minimum removals
        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        res = []
        path = []

        def dfs(i, left_rem, right_rem, open_cnt):
            if i == len(s):
                if left_rem == 0 and right_rem == 0 and open_cnt == 0:
                    res.append("".join(path))
                return

            ch = s[i]

            # Option 1: remove this char (dedupe: only remove first of a run)
            if ch == '(' and left_rem > 0:
                if i == 0 or s[i - 1] != '(' or True:
                    pass
            # Handle runs of identical parens to avoid duplicates
            if ch in "()":
                # Find the end of the run of identical chars
                j = i
                while j < len(s) and s[j] == ch:
                    j += 1
                run = j - i

                # Choose k chars to remove from this run (0..run)
                max_rem = left_rem if ch == '(' else right_rem
                for k in range(0, min(run, max_rem) + 1):
                    keep = run - k
                    new_open = open_cnt + (keep if ch == '(' else -keep)
                    if new_open < 0:
                        continue
                    path.append(ch * keep)
                    if ch == '(':
                        dfs(j, left_rem - k, right_rem, new_open)
                    else:
                        dfs(j, left_rem, right_rem - k, new_open)
                    path.pop()
            else:
                path.append(ch)
                dfs(i + 1, left_rem, right_rem, open_cnt)
                path.pop()

        dfs(0, left, right, 0)
        return res