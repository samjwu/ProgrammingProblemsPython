class Solution:
    def check(self, nums: List[int]) -> bool:
        decreases = 0

        n = len(nums)

        for i in range(n-1):
            if nums[i] > nums[i+1]:
                decreases += 1

        if nums[n-1] > nums[0]:
            decreases += 1

        return decreases <= 1
