class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
            
        n = len(s1)
        freq1 = [0] * 26
        freq2 = [0] * 26
        diffs = 0

        for i in range(n):
            c1 = s1[i]
            c2 = s2[i]

            if c1 != c2:
                diffs += 1

                if diffs > 2:
                    return False

            freq1[ord(c1) - ord("a")] += 1
            freq2[ord(c2) - ord("a")] += 1

        return diffs == 2 and freq1 == freq2
