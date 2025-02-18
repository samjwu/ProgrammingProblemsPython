class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        ans = []
        stk = []

        for i in range(n + 1):
            stk.append(i + 1)

            if i == n or pattern[i] == "I":
                while stk:
                    ans.append(str(stk.pop()))

        return "".join(ans)
