class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord('a')] += 1

        odd = 0
        for count in freq:
            if count % 2 == 1:
                odd += 1

        return odd <= k
