from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = Counter(str(n))

        # 32 bit integer
        for i in range(31):
            power_of_2 = 1 << i

            # if digits in n match digits in power of 2
            # then found an answer
            if Counter(str(power_of_2)) == digits:
                return True

        return False
