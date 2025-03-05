class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 1
        add = 4

        while n > 1:
            ans += add
            add += 4
            n -= 1

        return ans
