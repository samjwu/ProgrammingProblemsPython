class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        total = sum(derived)

        return total % 2 == 0
