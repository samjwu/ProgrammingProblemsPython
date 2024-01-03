class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        
        prevRow = 0
        
        for s in bank:
            currRow = 0
            
            for c in s:
                if c == "1":
                    currRow += 1
            
            if currRow > 0:
                ans += prevRow * currRow
                prevRow = currRow
        
        return ans
