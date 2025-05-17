class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zeroes = 0
        ones = 0

        for num in nums:
            if num == 0:
                zeroes += 1
            elif num == 1:
                ones += 1

        for i in range(0, zeroes):
            nums[i] = 0

        for i in range(zeroes, zeroes + ones):
            nums[i] = 1

        for i in range(zeroes + ones, n):
            nums[i] = 2
