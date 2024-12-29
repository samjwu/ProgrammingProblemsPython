class Solution:
    def __init__(self):
        self.MOD = int(10e9+7)

    def numWays(self, words: List[str], target: str) -> int:
        m = len(words[0])
        n = len(words)
        k = len(target)

        memo = [[-1] * k for i in range(m)]

        freq = [[0] * 26 for i in range(m)]

        for i in range(n):
            for j in range(m):
                char = ord(words[i][j]) - ord('a')
                freq[j][char] += 1

        return self.recurse(target, 0, 0, memo, freq, m, k)

    def recurse(self, target, wordIdx, targetIdx, memo, freq, m, k):
        if targetIdx == k:
            return 1

        # not enough chars in word len to hit target
        if wordIdx == m or m - wordIdx < k - targetIdx:
            return 0

        if memo[wordIdx][targetIdx] != -1:
            return memo[wordIdx][targetIdx]

        ans = 0
        cur = ord(target[targetIdx]) - ord('a')

        # skip current char in word lens
        ans += self.recurse(target, wordIdx + 1, targetIdx, memo, freq, m, k)
        
        # try all possible words at cur len
        # equiv to cur char freq times all remaining possibilities
        ans += freq[wordIdx][cur] * self.recurse(target, wordIdx + 1, targetIdx + 1, memo, freq, m, k)

        memo[wordIdx][targetIdx] = ans % self.MOD
        return memo[wordIdx][targetIdx]
