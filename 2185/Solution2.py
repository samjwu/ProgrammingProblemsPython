class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        m = len(pref)

        for word in words:
            if word[0:m] == pref:
                ans += 1

        return ans
