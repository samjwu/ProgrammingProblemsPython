class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        remainder = n % 7
        
        first_week = 28
        last_week = first_week + (weeks - 1) * 7
        
        ans = weeks * (first_week + last_week) // 2
        
        for i in range(remainder):
            ans += i + 1 + weeks
            
        return ans
