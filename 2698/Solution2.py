class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0

        for i in range(1, n + 1):
            square = i * i

            if self.valid_partition(str(square), i):
                ans += square

        return ans

    def valid_partition(self, s, target):
        if not s and target == 0:
            return True

        if target < 0:
            return False

        for index in range(len(s)):
            left = s[:index + 1]
            right = s[index + 1:]

            if self.valid_partition(right, target - int(left)):
                return True

        return False
