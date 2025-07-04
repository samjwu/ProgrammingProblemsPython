from typing import List

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        low1 = min(nums1)
        low2 = min(nums2)

        return low2 - low1
