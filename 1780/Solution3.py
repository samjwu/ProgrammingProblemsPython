class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            # if n in ternary has a 2
            # then a power of 3 is used twice
            # therefore nondistinct so return False
            if n % 3 == 2:
                return False

            n //= 3

        return True
