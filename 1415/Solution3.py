class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        stk = []
        idx = 0
        stk.append("")

        while stk:
            curr = stk.pop()

            if len(curr) == n:
                idx += 1

                if idx == k:
                    return curr

                continue

            # keep lexicographic order by pushing to stack in reverse
            for c in "cba":
                # skip duplicate chars
                if len(curr) == 0 or curr[-1] != c:
                    stk.append(curr + c)
                    
        return ""
