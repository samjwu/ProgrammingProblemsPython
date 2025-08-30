class Solution:
    def minChanges(self, n: int, k: int) -> int:
        changes = 0

        for i in range(32):
            if n & 1 != k & 1:
                changes += 1
                if k & 1 == 1:
                    return -1
            n >>= 1
            k >>= 1

        return changes
