class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return self.recurse(s, 0, seen)

    def recurse(self, s: str, idx: int, seen: set[str]) -> int:
        if idx == len(s):
            return 0

        ans = 0

        for i in range(idx+1, len(s)+1):
            substr = s[idx:i]

            if substr not in seen:
                # add candidate substring
                seen.add(substr)
                # recurse
                ans = max(ans, self.recurse(s, i, seen)+1)
                # backtrack
                seen.remove(substr)

        return ans
