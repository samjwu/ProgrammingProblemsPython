class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xorAll = 0

        for n in nums:
            xorAll ^= n

        ans = 0
        
        for i in range(32):
            if (k % 2) != (xorAll % 2):
                ans += 1

            k //= 2
            xorAll //= 2

        return ans
