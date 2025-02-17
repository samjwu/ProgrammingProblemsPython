class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = [0] * 26
        for c in tiles:
            freq[ord(c) - ord("A")] += 1

        return self.recurse(freq)

    def recurse(self, freq: list) -> int:
        ans = 0

        for i in range(26):
            if freq[i] == 0:
                continue

            # add candidate subanswer
            ans += 1

            # use char
            freq[i] -= 1
            ans += self.recurse(freq)
            # backtrack
            freq[i] += 1

        return ans
