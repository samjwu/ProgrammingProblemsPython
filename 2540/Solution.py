class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        
        i = 0
        j = 0
        
        while i < m and j < n and nums1[i] != nums2[j]:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        if i < m and j < n and nums1[i] == nums2[j]:
            return nums1[i]
        
        return -1
