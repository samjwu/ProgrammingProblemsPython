class Solution:
    def fractionAddition(self, expression: str) -> str:
        n = len(expression)

        numerator = 0
        denominator = 1

        i = 0

        while i < n:
            negative = False
            currNumerator = 0
            currDenominator = 0

            # sign
            if expression[i] == "-" or expression[i] == "+":
                if expression[i] == "-":
                    negative = True
                i += 1

            # numerator
            while i < n and expression[i].isdigit():
                val = int(expression[i])
                currNumerator = currNumerator * 10 + val
                i += 1

            if negative:
                currNumerator *= -1

            # division symbol
            i += 1

            # denominator
            while i < n and expression[i].isdigit():
                val = int(expression[i])
                currDenominator = currDenominator * 10 + val
                i += 1

            numerator = numerator * currDenominator + currNumerator * denominator
            denominator = denominator * currDenominator

        gcd = abs(self.gcd(numerator, denominator))

        numerator //= gcd
        denominator //= gcd

        return f"{numerator}/{denominator}"

    def gcd(self, a: int, b: int) -> int:
        if a == 0:
            return b

        return self.gcd(b % a, a)
