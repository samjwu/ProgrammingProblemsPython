class Solution:
    def countKeyChanges(self, s: str) -> int:
        n = len(s)
        ans = 0
        prev = s[0]

        for i in range(1, n):
            if prev.lower() != s[i].lower():
                ans += 1
            prev = s[i]

        return ans
