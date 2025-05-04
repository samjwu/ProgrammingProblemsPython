class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen = {}
        ans = 0

        for domino in dominoes:
            a = min(domino[0], domino[1])
            b = max(domino[0], domino[1])

            if (a, b) in seen:
                ans += seen[(a, b)]
                seen[(a, b)] += 1
            else:
                seen[(a, b)] = 1

        return ans
