class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        exponent = 0

        while 3**exponent <= n:
            exponent += 1

        while n > 0:
            if n >= 3**exponent:
                n -= 3**exponent
            
            if n >= 3**exponent:
                return False

            exponent -= 1

        return True
