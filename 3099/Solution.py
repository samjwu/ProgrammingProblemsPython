class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digit_sum = 0
        tmp = x

        while tmp > 0:
            digit_sum += tmp % 10
            tmp = tmp // 10

        if x % digit_sum == 0:
            return digit_sum
        return -1
