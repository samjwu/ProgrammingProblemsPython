class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)

        total = sum(rolls)
        
        remaining = mean * (m+n) - total
        
        if remaining > 6 * n or remaining < n:
            return []

        remainingAvg = remaining // n

        remainder = remaining % n
        
        ans = [remainingAvg] * n
        
        for i in range(remainder):
            ans[i] += 1

        return ans
