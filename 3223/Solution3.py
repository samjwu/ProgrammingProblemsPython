class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        
        freq = [0] * 26

        for c in s:
            order = ord(c) - ord('a')
            freq[order] += 1

        deleted = 0

        for count in freq:
            if count <= 2:
                continue
                
            if count % 2 == 1:
                deleted += count - 1
            else:
                deleted += count - 2

        return n - deleted
