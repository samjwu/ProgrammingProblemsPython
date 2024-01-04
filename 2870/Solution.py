class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        
        freq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1
        
        for k in freq.keys():
            if freq[k] == 1: 
                return -1
            
            ans += ceil(freq[k] / 3)
            
        return ans
