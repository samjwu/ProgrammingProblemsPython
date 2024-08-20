class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        memo = [[0 for j in range(n)] for i in range(n)]

        suffix = piles[:]

        for i in range(n-2, -1, -1):
            suffix[i] += suffix[i + 1]

        return self.recurse(suffix, 1, n, 0, memo)

    def recurse(self, suffix: List[int], m: int, n: int, idx: int, memo: List[List[int]]) -> int:
        # take all remaining stones if current index + 2M >= n
        if idx + 2 * m >= len(suffix):
            return suffix[idx]

        if memo[idx][m] > 0:
            return memo[idx][m]

        # to get answer for alice, minimize answer for bob
        bob = float("inf")

        # try all bob's possibilities
        for i in range(1, 1 + 2*m):
            bob = min(bob, self.recurse(suffix, max(i, m), n, idx + i, memo))

        memo[idx][m] = suffix[idx] - bob

        return memo[idx][m]
