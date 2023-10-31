class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        arr_sum = sum(nums)
        
        ans = sum(i * j for i, j in enumerate(nums))
        curr = ans
        
        while nums:
            curr = curr + arr_sum - (nums.pop() * n)
            ans = max(ans, curr)
            
        return ans
