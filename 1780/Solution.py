class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return self.recurse(0, n)

    def recurse(self, exponent: int, n: int) -> bool:
        if n == 0:
            return True

        if 3**exponent > n:
            return False

        take = self.recurse(exponent + 1, n - 3**exponent)
        skip = self.recurse(exponent + 1, n)

        return take or skip
