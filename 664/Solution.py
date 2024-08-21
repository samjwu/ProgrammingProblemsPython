class Solution:
    def strangePrinter(self, s: str) -> int:
        # remove duplicate chars
        reduced = s[0]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                reduced += s[i]

        memo = {}

        def calcMinTurns(start: int, end: int) -> int:
            if start > end:
                return 0

            if (start, end) in memo:
                return memo[(start, end)]

            # worst case: ans = length of string
            ans = 1 + calcMinTurns(start + 1, end)

            # look for matches
            for k in range(start + 1, end + 1):
                if reduced[k] == reduced[start]:
                    # split string into subproblems
                    left = calcMinTurns(start, k - 1)
                    right = calcMinTurns(k + 1, end)
                    candidate = left + right
                    ans = min(ans, candidate)

            memo[(start, end)] = ans

            return ans

        return calcMinTurns(0, len(reduced) - 1)
