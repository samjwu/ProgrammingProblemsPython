class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        ans = 0

        if n % 2 == 1:
            for num in nums1:
                ans = ans ^ num

        if m % 2 == 1:
            for num in nums2:
                ans = ans ^ num

        return ans
