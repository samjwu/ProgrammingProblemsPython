class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # return 0 if finding an impossible number of inversions
        # n * (n-1) total pairings
        # n * (n-1) / 2 since only half can be inversions
        if k > n * (n-1) / 2:
            return 0
        
        # return 1 if minimum inversions (sequential ascending)
        # or maximum inversions (descending)
        if k == 0 or k == n * (n-1) /2:
            return 1
        
        MOD = 1e9 + 7
        
        memo = [[0 for j in range(k+1)] for i in range(n+1)]
        memo[2][0] = 1
        memo[2][1] = 1
        
        # memo[n][k+1] = memo[n][k] + memo[n-1][k+1] - memo[n-1][k+1-n]
        for i in range(3, n+1):
            memo[i][0] = 1
            
            for j in range(1, k+1):
                memo[i][j] = memo[i][j-1] + memo[i-1][j]
                
                if j >= i:
                    memo[i][j] -= memo[i-1][j-i]
                    
                memo[i][j] = (memo[i][j] + MOD) % MOD
                
        return int(memo[i][j])
