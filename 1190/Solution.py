class Solution:
    def reverseParentheses(self, s: str) -> str:
        # store indices of open brackets
        stk = []
        
        ans = []

        for c in s:
            if c == "(":
                # store full len of current ans
                # since everything after current ans gets reversed
                stk.append(len(ans))
            elif c == ")":
                start = stk.pop()
                ans[start:] = ans[start:][::-1]
            else:
                ans.append(c)
        
        return "".join(ans)
