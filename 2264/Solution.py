class Solution:
    def largestGoodInteger(self, num: str) -> str:
        hi = -1
        
        n = len(num)
        
        for i in range(n-2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                hi = max(hi, int(num[i]))
        
        if hi > -1:
            return str(hi) * 3
        
        return ""
