class Solution:
    def getSmallestString(self, s: str) -> str:
        n = len(s)
        chars = [c for c in s]

        for i in range(n-1):
            if chars[i] > chars[i+1] and int(chars[i]) % 2 == int(chars[i+1]) % 2:
                chars[i], chars[i+1] = chars[i+1], chars[i]
                break

        return "".join(chars)
