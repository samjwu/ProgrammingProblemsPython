class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        zeroes = 0
        ones = 0
        substrings = 0

        left = 0
        for right in range(n):
            if s[right] == '0':
                zeroes += 1
            else:
                ones += 1

            while zeroes > k and ones > k:
                if s[left] == '0':
                    zeroes -= 1
                else:
                    ones -= 1
                left += 1

            substrings += right - left + 1

        return substrings
