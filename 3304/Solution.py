class Solution:
    def kthCharacter(self, k: int) -> str:
        chars = ['a']

        while len(chars) < k:
            n = len(chars)
            
            for i in range(n):
                next_char = chr(ord('a') + ((ord(chars[i]) - ord('a') + 1) % 26))
                chars.append(next_char)

        return chars[k - 1]
