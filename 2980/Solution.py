class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                bitwise_or = nums[i] | nums[j]
                if 1 & bitwise_or == 0:
                    return True

        return False
