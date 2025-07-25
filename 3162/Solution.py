from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = 0
        nums2k = [num * k for num in nums2]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2k[j]) == 0:
                    pairs += 1

        return pairs
