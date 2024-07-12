class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0

        # greedy: remove higher scoring substring first
        if x > y:
            hi = "ab"
            lo = "ba"
        else:
            hi = "ba"
            lo = "ab"

        s2 = self.removeSubstr(s, hi)
        removed = (len(s) - len(s2)) // 2
        ans += removed * max(x, y)

        s3 = self.removeSubstr(s2, lo)
        removed = (len(s2) - len(s3)) // 2
        ans += removed * min(x, y)

        return ans

    def removeSubstr(self, s: str, pair: str) -> str:
        stk = []

        for c in s:
            if (c == pair[1] and len(stk) > 0 and stk[-1] == pair[0]):
                stk.pop()
            else:
                stk.append(c)

        return "".join(stk)
