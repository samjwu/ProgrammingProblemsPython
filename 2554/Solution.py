class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        bans = set(banned)
        
        runningSum = 0
        ans = 0
        
        for i in range(1, n+1):
            if i in bans:
                continue
                
            if runningSum + i <= maxSum:
                runningSum += i
                ans += 1
            else:
                return ans
        
        return ans
