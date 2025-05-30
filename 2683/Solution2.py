class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor = 0

        for num in derived:
            xor = xor ^ num

        return xor == 0
