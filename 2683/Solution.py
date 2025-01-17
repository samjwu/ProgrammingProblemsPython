class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)

        original = [0]
        for i in range(n):
            original.append(derived[i] ^ original[i])
        start_with_0 = original[0] ^ original[n-1] == derived[n-1]

        original = [1]
        for i in range(n):
            original.append(derived[i] ^ original[i])
        start_with_1 = original[0] ^ original[n-1] == derived[n-1]

        return start_with_0 or start_with_1
