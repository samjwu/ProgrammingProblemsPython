class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        ans = 0
        
        remainder = 0
        
        # map remainder to number of times it was seen
        seenRemainders = [0 for i in range(k)]
        # base case
        seenRemainders[0] = 1
        
        for i in range(n):
            remainder = (remainder + (nums[i] % k) + k) % k
            
            # if curr subarray has rem matching a prev subarray
            # then each instance is a subans
            ans += seenRemainders[remainder]
            
            seenRemainders[remainder] += 1
            
        return ans
