class Solution:
    def maximum69Number(self, num: int) -> int:
        digits = [digit for digit in str(num)]
        n = len(digits)

        for i in range(n):
            if digits[i] == '6':
                digits[i] = '9'
                return int("".join(digits))

        return num
