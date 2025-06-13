class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        pairs1 = set(pairwise(s))
        pairs2 = set(pairwise(s[::-1]))

        return bool(pairs1 & pairs2)
