class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0] * 26
        
        for c in s:
            freq[ord(c) - ord('a')] += 1

        odd = 0
        even = float('inf')

        for f in freq:
            if f == 0:
                continue

            if f % 2 == 1:
                odd = max(odd, f)
            else:
                even = min(even, f)

        return odd - even
