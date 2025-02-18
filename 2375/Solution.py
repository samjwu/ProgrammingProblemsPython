class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)

        s = "".join(str(num) for num in range(1, n + 2))

        for permutation in permutations(s):
            permutation_str = "".join(permutation)

            if self.isValid(permutation_str, pattern):
                return permutation_str

        return ""
        
    def isValid(self, s: str, pattern: str) -> bool:
        for index in range(len(pattern)):
            if pattern[index] == "I" and s[index] > s[index + 1]:
                return False
            elif pattern[index] == "D" and s[index] < s[index + 1]:
                return False

        return True
