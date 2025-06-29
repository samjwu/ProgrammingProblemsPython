class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [False] * 26
        upper = [False] * 26

        for c in word:
            if c >= 'a' and c <= 'z':
                index = ord(c) - ord('a')
                lower[index] = True
            else:
                index = ord(c) - ord('A')
                upper[index] = True

        special = 0

        for i in range(26):
            if lower[i] and upper[i]:
                special += 1

        return special
