class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)

        # memo[i][c] = longest substr len up to ith char in s ending at char c
        memo = [[-1 for j in range(26)] for i in range(n)]

        def dfs(i: int, c: int) -> int:
            if memo[i][c] != -1:
                return memo[i][c]

            # base case: ith char does not match c
            memo[i][c] = 0

            # base case: ith char matches c
            if c == (ord(s[i]) - ord('a')):
                memo[i][c] = 1

            # dfs from ith char to 0th char
            if i > 0:
                memo[i][c] = dfs(i - 1, c)

                # append ith char if it matches c
                if c == (ord(s[i]) - ord('a')):
                    # try all subanswers ending with prev char
                    # append ith char if diff is within k
                    for prev in range(26):
                        if abs(c - prev) <= k:
                            memo[i][c] = max(memo[i][c], dfs(i - 1, prev) + 1)

            return memo[i][c]

        ans = 0

        # try all chars in alphabet, starting from end of s
        for c in range(26):
            ans = max(ans, dfs(n - 1, c))

        return ans
