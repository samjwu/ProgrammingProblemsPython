class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        idx = 0
        for num in nums:
            if num != 0:
                nums[idx] = num
                idx += 1
        
        while idx < n:
            nums[idx] = 0
            idx += 1

        return nums
