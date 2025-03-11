class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        prev = [-1] * 3

        for i in range(n):
            prev[ord(s[i]) - ord("a")] = i

            # if any is -1 (not seen), return 0
            # otherwise, return leftmost seen
            # and all substrings by adding everything before leftmost
            ans += 1 + min(prev)

        return ans
