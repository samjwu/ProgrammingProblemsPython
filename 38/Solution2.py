class Solution:
    def countAndSay(self, n: int) -> str:
        def recurse(s, m):
            if m == n:
                return s

            c = s[0]
            count = 1
            ans = ""

            for i in range(1, len(s)):
                if s[i] == c[0]:
                    count += 1
                else:
                    ans += str(count) + c
                    c = s[i]
                    count = 1
            ans += str(count) + c

            return recurse(ans, m+1)

        return recurse("1", 1)
