class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        key = 0
        multiplier = 1

        while multiplier <= 1000:
            key += multiplier * min(num1 // multiplier % 10, num2 // multiplier % 10, num3 // multiplier % 10)
            multiplier *= 10

        return key
