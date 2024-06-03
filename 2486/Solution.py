class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        idx = 0
        longestPrefix = 0

        # greedy: count the longest prefix of s
        # that appears in t as a subsequence
        while idx < n and longestPrefix < m:
            if s[idx] == t[longestPrefix]:
                longestPrefix += 1
            idx += 1

        return m - longestPrefix
