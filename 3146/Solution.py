class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        n = len(s)
        s_indices = [-1] * 26
        t_indices = [-1] * 26
        perm_diff = 0

        for i in range(n):
            s_indices[ord(s[i]) - ord('a')] = i
            t_indices[ord(t[i]) - ord('a')] = i

        for i in range(26):
            perm_diff += abs(s_indices[i] - t_indices[i])

        return perm_diff
