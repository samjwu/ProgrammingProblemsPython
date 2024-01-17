class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums = set()
        freq = defaultdict(int)
        
        for num in arr:
            nums.add(num)
            freq[num] += 1
            
        occs = set()
            
        for num in nums:
            if freq[num] in occs:
                return False
            
            occs.add(freq[num])
            
        return True
