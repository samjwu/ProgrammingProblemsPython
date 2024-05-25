class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)

        currSentence = []

        ans = []

        self.recurse(s, wordSet, currSentence, ans, 0)

        return ans
        
    def recurse(
        self,
        s: str,
        wordSet: set,
        curr: List[str],
        ans: List[str],
        idx: int,
    ) -> None:
        if idx == len(s):
            ans.append(" ".join(curr))
            return

        for end in range(idx + 1, len(s) + 1):
            word = s[idx:end]

            if word in wordSet:
                curr.append(word)

                self.recurse(s, wordSet, curr, ans, end)

                # backtrack
                curr.pop()
