import bisect

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = len(nums) - bisect.bisect_right(nums, 0)
        neg = bisect.bisect_left(nums, 0)
        return max(pos, neg)
