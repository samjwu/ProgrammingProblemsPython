class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xorAll = 0

        for n in nums:
            xorAll ^= n

        return bin(xorAll ^ k).count('1')
