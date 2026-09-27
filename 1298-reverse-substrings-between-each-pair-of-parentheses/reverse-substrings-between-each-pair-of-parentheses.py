class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']  # stack[-1] is the current "active" string being built

        for ch in s:
            if ch == '(':
                stack.append('')
            elif ch == ')':
                top = stack.pop()
                stack[-1] += top[::-1]
            else:
                stack[-1] += ch

        return stack[0]