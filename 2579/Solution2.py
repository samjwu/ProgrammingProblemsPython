class Solution:
    def coloredCells(self, n: int) -> int:
        # start with 1
        # adding 4 each time
        # 1 + 4*1 + 4*2 + ... + 4*(n-1)
        # arithmetic series sum = n*(n-1)/2
        # therefore 4 * (n*(n-1)/2)
        # simplifies to 2 * n * (n-1)
        return 1 + 2 * n * (n-1)
