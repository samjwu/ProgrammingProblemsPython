class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(2, n):
            max_i = nums[0]
            
            for j in range(1, k):
                ans = max(ans, (max_i - nums[j]) * nums[k])
                max_i = max(max_i, nums[j])

        return ans
