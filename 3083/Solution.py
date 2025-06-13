class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        pairs = set()
        n = len(s)

        for i in range(n-1):
            substr = s[i:i+2]
            pairs.add(substr)

        rev = s[::-1]

        for pair in pairs:
            if pair in rev:
                return True

        return False
