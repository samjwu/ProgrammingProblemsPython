class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1e9 + 7

        memo = {}
        memo[1] = 1;
        memo[2] = 2;
        memo[3] = 5;

        for i in range(4, n+1):
            memo[i] = 2 * memo[i-1] + memo[i-3]
            memo[i] %= MOD
        
        return int(memo[n])
