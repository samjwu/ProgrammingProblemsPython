class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        freq = [0] * 26
        l = 0
        r = 0
        max_len = 2

        while r < n:
            char_index = ord(s[r]) - ord('a')
            freq[char_index] += 1

            while freq[char_index] > 2:
                old_char_index = ord(s[l]) - ord('a')
                freq[old_char_index] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
