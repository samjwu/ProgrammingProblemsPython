class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = len(nums) - self.bisect_right(nums, 0)
        neg = self.bisect_left(nums, 0)

        return max(pos, neg)

    def bisect_left(self, nums, target):
        l = 0
        r = len(nums)
        index = len(nums)

        while l < r:
            m = l + (r-l) // 2

            if nums[m] < target:
                l = m + 1
            else:
                r = m

        return l

    def bisect_right(self, nums, target):
        l = 0
        r = len(nums)
        index = len(nums)

        while l < r:
            m = l + (r-l) // 2

            if nums[m] <= target:
                l = m + 1
            else:
                r = m

        return l
