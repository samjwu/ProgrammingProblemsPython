class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        chars = []

        for i in range(n):
            idx = (i + k) % n
            chars.append(s[idx])

        return "".join(chars)
