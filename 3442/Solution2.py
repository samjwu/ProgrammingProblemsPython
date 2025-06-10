from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)

        odd = max(f for f in freq.values() if f % 2 == 1)
        even = min(f for f in freq.values() if f % 2 == 0)

        return odd - even
