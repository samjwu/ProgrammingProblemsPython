class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_i = 0
        max_i_minus_j = 0
        ans = 0

        for k in range(n):
            # check for candidate answer
            ans = max(ans, max_i_minus_j * nums[k])
            # check for highest i - j
            max_i_minus_j = max(max_i_minus_j, max_i - nums[k])
            # check for highest i
            max_i = max(max_i, nums[k])
        
        return ans
