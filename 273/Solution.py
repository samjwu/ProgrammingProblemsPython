class Solution:
    # store unique words for numbers
    # use exclusive end range for naming convention
    zeroToTen = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tenToTwenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    zeroToOneHundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
            
        return self.recurse(num)

    def recurse(self, num: int) -> str:
        # break at unique words for numbers

        # 0-9
        if num < 10:
            return self.zeroToTen[num]

        # 10-19
        if num < 20:
            return self.tenToTwenty[num - 10]

        # 19-99
        if num < 100:
            tens = self.zeroToOneHundred[num // 10]

            units = ""
            if num % 10 != 0:
                units = " " + self.recurse(num % 10)

            return tens + units

        # 100-999
        if num < 1000:
            hundreds = self.recurse(num // 100)

            remainder = ""
            if num % 100 != 0:
                remainder = " " + self.recurse(num % 100)

            return hundreds + " Hundred" + remainder

        # 1,000-999,999
        if num < 1000000:
            thousands = self.recurse(num // 1000)

            remainder = ""
            if num % 1000 != 0:
                remainder = " " + self.recurse(num % 1000)

            return thousands + " Thousand" + remainder

        # 1,000,000-999,999,999
        if num < 1000000000:
            millions = self.recurse(num // 1000000)

            remainder = ""
            if num % 1000000 != 0:
                remainder = " " + self.recurse(num % 1000000)

            return millions + " Million" + remainder

        # over 1,000,000,000
        billions = self.recurse(num // 1000000000)

        remainder = ""
        if num % 1000000000 != 0:
            remainder = " " + self.recurse(num % 1000000000)

        return billions + " Billion" + remainder
