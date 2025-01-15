class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        ans = num1

        bits1 = bin(num1).count("1")
        bits2 = bin(num2).count("1")

        def add_bits(diff, val):
            idx = 0
            while diff:
                if (num1 & (1 << idx)) == 0:
                    val |= (1 << idx)
                    diff -= 1
                idx += 1
            return val

        def remove_bits(diff, val):
            idx = 0
            while diff:
                if (num1 & (1 << idx)) != 0:
                    val &= ~(1 << idx)
                    diff -= 1
                idx += 1
            return val

        if bits1 < bits2:
            ans = add_bits(bits2 - bits1, num1)
        elif bits1 > bits2:
            ans = remove_bits(bits1 - bits2, num1)

        return ans
