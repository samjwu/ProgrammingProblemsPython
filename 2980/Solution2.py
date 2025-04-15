class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        n = len(nums)
        evens = 0

        for i in range(n):
            if nums[i] % 2 == 0:
                evens += 1

        return evens >= 2
