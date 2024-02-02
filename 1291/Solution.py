class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        
        n = len(digits)
        
        ans = []
        
        for i in range(n):
            for j in range(i+1, n):
                num = int(digits[i:j+1])
                
                if num >= low and num <= high:
                    ans.append(num)
                    
        ans.sort()
                    
        return ans       
