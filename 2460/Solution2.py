class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        idx = 0

        for i in range(n):
            if i+1 < n and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

            if nums[i]:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1

        return nums
