class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        
        exp = 0
        
        while num > 0:
            if (num & 1) == 0:
                ans |= 1 << exp
                
            exp += 1
            
            num = num >> 1
            
        return ans
