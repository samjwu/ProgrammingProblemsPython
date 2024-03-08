class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        
        ans = []
        
        hi = 0
        
        for num in nums:
            freq[num] += 1
            
            if freq[num] > hi:
                hi = freq[num]
                ans = [num]
            elif freq[num] == hi:
                ans.append(num)
        
        return len(ans) * hi
