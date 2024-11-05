class Solution:
    def minChanges(self, s: str) -> int:
        curr = s[0]

        count = 0

        ans = 0

        for c in s:
            # same char, continue
            if c == curr:
                count += 1
                continue

            # new char, check for length parity
            # add 1 to ans if parity is odd
            if count % 2 == 0:
                count = 1
            else:
                count = 0
                ans += 1

            curr = c

        return ans
