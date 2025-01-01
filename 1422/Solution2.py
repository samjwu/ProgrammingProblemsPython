class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zeroes = [0] * n
        ones = [0] * n

        for i in range(n):
            if i > 0:
                zeroes[i] = zeroes[i-1]
                ones[i] = ones[i-1]
                
            if s[i] == "0":
                zeroes[i] += 1
            else:
                ones[i] += 1

        ans = 0

        for i in range(1, n):
            left = zeroes[i-1]
            right = ones[n-1] - ones[i-1]
            ans = max(ans, left + right)

        return ans
