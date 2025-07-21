class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        chars = [c for c in s]
        j = 2

        for i in range(2, n):
            if chars[i] != chars[j-1] or chars[i] != chars[j-2]:
                chars[j] = chars[i]
                j += 1

        return "".join(chars[0:j])
