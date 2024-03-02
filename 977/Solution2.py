class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        
        i = 0
        j = len(nums)-1
        
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                ans.append(nums[j] * nums[j])
                j -= 1
            else:
                ans.append(nums[i] * nums[i])
                i += 1
        
        ans.reverse()
        
        return ans
