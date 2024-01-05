class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        memo = [1] * n
        
        for j in range(n):
            for i in range(j):
                if nums[i] < nums[j] and memo[i] + 1 > memo[j]:
                    memo[j] = memo[i] + 1
                    
        return max(memo)
