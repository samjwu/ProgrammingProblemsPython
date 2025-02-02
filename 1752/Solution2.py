class Solution:
    def check(self, nums: List[int]) -> bool:
        decreases = 0

        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                decreases += 1

        return decreases <= 1
