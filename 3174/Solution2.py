class Solution:
    def clearDigits(self, s: str) -> str:
        n = len(s)
        s = [c for c in s]
        ans_len = 0

        for i in range(n):
            if s[i].isdigit():
                ans_len = max(ans_len - 1, 0)
            else:
                s[ans_len] = s[i]
                ans_len += 1

        s = s[:ans_len]

        return "".join(s)
