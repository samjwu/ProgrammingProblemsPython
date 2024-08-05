class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = defaultdict(int)
        
        for s in arr:
            freq[s] += 1
            
        distinct = 0
            
        for s in arr:
            if freq[s] == 1:
                distinct += 1
                
                if distinct == k:
                    return s
                
        return ""
