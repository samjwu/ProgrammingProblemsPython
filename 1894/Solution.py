class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        
        total = 0
        
        # sim until chalk used up
        for i in range(n):
            total += chalk[i]
            if total > k:
                break
                
        # find remainder of usage
        k = k % total
        
        for i in range(n):
            if k < chalk[i]:
                return i
            
            k -= chalk[i]
            
        return 0
