class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        diffs = 0
        idx1 = 0
        idx2 = 0

        for i in range(n):
            if s1[i] != s2[i]:
                diffs += 1

                if diffs > 2:
                    return False
                elif diffs == 1:
                    idx1 = i
                else: # diffs == 2
                    idx2 = i
        
        return s1[idx1] == s2[idx2] and s1[idx2] == s2[idx1]
