class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        chars = list(s)
        write_idx = 2

        for i in range(2, n):
            if chars[i] != chars[write_idx-1] or chars[i] != chars[write_idx-2]:
                chars[write_idx] = chars[i]
                write_idx += 1

        return "".join(chars[0:write_idx])
