class Solution:
    def getLucky(self, s: str, k: int) -> int:
        t = ""
        for c in s:
            t += str(ord(c) - ord("a") + 1)
            
        while k > 0:
            digits = 0
            
            for digit in t:
                digits += int(digit)
                
            t = str(digits)
                
            k -= 1
            
        return int(t)
