class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        count = 1

        for i in range(1, n):
            if word[i-1] == word[i]:
                count += 1

        return count
