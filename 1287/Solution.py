class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        
        freq = defaultdict(int)
        
        for num in arr:
            freq[num] += 1
            
            if freq[num] > n / 4:
                return num
            
        return -1
