class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        # keep track of highest i and k at each index
        max_i = [0] * n
        max_k = [0] * n

        for i in range(1, n):
            max_i[i] = max(max_i[i-1], nums[i-1])
            max_k[n-1-i] = max(max_k[n-i], nums[n-i])

        ans = 0
        
        for j in range(1, n-1):
            ans = max(ans, (max_i[j] - nums[j]) * max_k[j])

        return ans
