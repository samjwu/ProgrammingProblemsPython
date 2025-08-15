class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        return n > 0 and n & (n - 1) == 0 and n % 3 == 1
