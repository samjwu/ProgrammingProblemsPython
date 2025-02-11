class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stk = []
        m = len(part)

        for c in s:
            stk.append(c)

            if len(stk) >= m and self.found_occurence(stk, part, m):
                for i in range(m):
                    stk.pop()

        return "".join(stk)

    def found_occurence(self, stk: list, part: str, m: int) -> bool:
        return "".join(stk[-m:]) == part
