class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = defaultdict(int)
        
        for num in nums1:
            seen[num] += 1
        
        ans = []
        
        for num in nums2:
            if seen[num] > 0:
                ans.append(num)
                seen[num] -= 1
                
        return ans
