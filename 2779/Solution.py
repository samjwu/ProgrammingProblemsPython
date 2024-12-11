class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        hi = max(nums)
        
        if 2*k >= hi:
            return len(nums)
        
        # prefix sum of count of numbers
        prefixFreq = [0] * (hi+1)
        
        for num in nums:
            prefixFreq[num] += 1
            
        for i in range(1, hi+1):
            prefixFreq[i] += prefixFreq[i-1]
            
        # check the first range
        ans = prefixFreq[2*k]
        
        # check remaining ranges
        # range is from [left, right]
        # where left is some num-k
        # and right is some num+k
        for right in range(2*k+1, hi+1):
            left = right - 2*k
            inRange = prefixFreq[right] - prefixFreq[left-1]
            ans = max(ans, inRange)
        
        return ans
