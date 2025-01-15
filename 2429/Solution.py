class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        ans = num1

        bits1 = bin(num1).count("1")
        bits2 = bin(num2).count("1")

        idx = 0

        if bits1 < bits2:
            diff = bits2 - bits1
            while diff:
                if (num1 & (1 << idx)) == 0:
                    ans |= (1 << idx)
                    diff -= 1
                idx += 1
        elif bits1 > bits2:
            diff = bits1 - bits2
            while diff:
                if (num1 & (1 << idx)) != 0:
                    ans &= ~(1 << idx)
                    diff -= 1
                idx += 1

        return ans
