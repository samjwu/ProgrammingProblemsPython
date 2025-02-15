class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0

        for i in range(1, n + 1):
            square = i * i

            if self.valid_partition(square, i):
                ans += square

        return ans

    def valid_partition(self, num, target):
        if target < 0 or num < target:
            return False

        if num == target:
            return True

        # use integer division to extract left
        # use modulo operator to extract right
        return (
            self.valid_partition(num // 10, target - num % 10)
            or self.valid_partition(num // 100, target - num % 100)
            or self.valid_partition(num // 1000, target - num % 1000)
        )
