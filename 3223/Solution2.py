from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        
        freq = Counter(s)

        deleted = 0

        for count in freq.values():
            if count % 2 == 1:
                deleted += count - 1
            else:
                deleted += count - 2

        return n - deleted
