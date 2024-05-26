class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1e9 + 7

        memo = [[[-1 for k in range(3)] for j in range(2)] for i in range(n+1)]

        def recurse(n: int, absentCount: int, consecLates: int) -> int:
            if absentCount >= 2 or consecLates >= 3:
                return 0
                
            if n == 0:
                return 1
            
            if memo[n][absentCount][consecLates] != -1:
                return memo[n][absentCount][consecLates]
                
            # try checking for all cases
            present = recurse(n - 1, absentCount, 0)
            absent = recurse(n - 1, absentCount + 1, 0)
            late = recurse(n - 1, absentCount, consecLates + 1)

            # subanswer is sum of all cases
            subans = ((present + absent) % MOD + late) % MOD
            
            memo[n][absentCount][consecLates] = subans

            return subans
            
        return int(recurse(n, 0, 0))
