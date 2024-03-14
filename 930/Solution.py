class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        
        n = len(nums)
        
        # prefixFreq[x] = number of prefix sums with sum x
        prefixFreq = {}
        # inital empty array
        prefixFreq[0] = 1
        
        runningSum = 0
        
        for i in range(n):
            runningSum += nums[i]
            
            if runningSum - goal in prefixFreq:
                ans += prefixFreq[runningSum - goal]
                
            prefixFreq[runningSum] = prefixFreq.get(runningSum, 0) + 1
                    
        return ans
