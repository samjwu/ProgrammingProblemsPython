class Solution:
    def findComplement(self, num: int) -> int:
        def toBinary(num: int) -> str:
            s = ""
            
            while num > 0:
                s += str(num % 2)
                num = num >> 1
            
            return s[::-1]
        
        def toNum(st: string) -> int:
            ans = 0
            
            for s in st:
                ans *= 2
                
                if s == "1":
                    ans += 1
            
            return ans
        
        binary = toBinary(num)
        
        complement = ""
        
        for bit in binary:
            if bit == "0":
                complement += "1"
            else:
                complement += "0"
        
        return toNum(complement)
