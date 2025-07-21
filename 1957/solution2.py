class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        chars = list(s)
        write_idx = 2

        for read_idx in range(2, n):
            if chars[read_idx] != chars[write_idx-1] or chars[read_idx] != chars[write_idx-2]:
                chars[write_idx] = chars[read_idx]
                write_idx += 1

        return "".join(chars[0:write_idx])
