class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        ans = []
        
        n = len(nums)
        
        nums.sort()
        
        # memo[i] = largest subset up to i
        memo = [1 for i in range(n)]
        
        # prev[i] = index of second largest element of largest subset up to i
        prev = [-1 for i in range(n)]
        
        # index of largest element of largest subset
        maxIdx = 0
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and memo[i] < memo[j] + 1:
                    memo[i] = memo[j] + 1
                    prev[i] = j
                    
            if memo[i] > memo[maxIdx]:
                maxIdx = i
        
        # idx tracks largest to smallest element of largest subset
        idx = maxIdx
        while idx >= 0:
            ans.append(nums[idx])
            idx = prev[idx]
        
        return ans
