class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if x <= 0:
            return -1

        digit_sum = 0
        value = x

        while value > 0:
            digit_sum += value % 10
            value = value // 10

        if x % digit_sum == 0:
            return digit_sum
        return -1
