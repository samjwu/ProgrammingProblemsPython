class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        
        ans = 0
        window_sum = 0
        
        left = 0
        for right in range(n):
            target = nums[right]
            window_sum += target
            
            while (right - left + 1) * target - window_sum > k:
                window_sum -= nums[left]
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans
