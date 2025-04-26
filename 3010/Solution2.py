class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        
        nums_sorted = sorted(nums[1:n])

        return nums[0] + nums_sorted[0] + nums_sorted[1]
