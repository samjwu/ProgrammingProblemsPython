class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        for i in range(low, high + 1):
            if self.is_symmetric(str(i)):
                ans += 1

        return ans

    def is_symmetric(self, s: str) -> bool:
        n = len(s)

        if n % 2 == 1:
            return False

        left = 0
        right = 0

        for i in range(0, n // 2):
            left += int(s[i])

        for i in range(n // 2, n):
            right += int(s[i])

        return left == right
