class Solution:
    def countDigitOne(self, n: int) -> int:
        ones = 0
        power_of_ten = 1

        while power_of_ten <= n:
            quotient, remainder = divmod(n, power_of_ten * 10)

            # Count ones from quotient
            # Each (power_of_ten*10) range contributes power_of_ten ones
            # Essentially the ones directly to the right of power_of_ten*10
            # ex: 110, 111, ..., 119
            ones += quotient * power_of_ten

            # Count ones in remainder
            # Contribution is capped at
            # remainder - power_of_ten + 1 (leftover numbers)
            # ex for 212: 210, 211, 212
            # or power_of_ten (the full ones block)
            # ex for 222: 210, 211, ..., 219
            if remainder >= power_of_ten:
                ones += min(remainder - power_of_ten + 1, power_of_ten)

            power_of_ten *= 10

        return ones
