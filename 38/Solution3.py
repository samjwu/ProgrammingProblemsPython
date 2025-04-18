class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        s = self.countAndSay(n-1)
        ans = ""
        c = s[0]
        count = 1

        for i in range(1, len(s)):
            if s[i] == c:
                count += 1
            else:
                ans += str(count) + c
                c = s[i]
                count = 1
        ans += str(count) + c

        return ans
