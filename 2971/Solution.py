class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        running_sum = 0
        
        ans = -1
        
        for num in nums:
            if num < running_sum:
                ans = num + running_sum
                
            running_sum += num
            
        return ans
