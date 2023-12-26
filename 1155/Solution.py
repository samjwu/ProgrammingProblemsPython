class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.mod = 1e9 + 7
        
        self.memo = [[-1 for j in range(target+1)] for i in range(n+1)]
        
        return self.recurse(n, k, target)
    
    def recurse(self, dice: int, faces: int, remainder: int) -> int:
        if dice == 0 or remainder <= 0:
            return dice == remainder
        
        if self.memo[dice][remainder] != -1:
            return self.memo[dice][remainder]
        
        subans = 0
        
        for i in range(1, faces+1):
            subans += self.recurse(dice - 1, faces, remainder - i)
            subans %= self.mod
        
        self.memo[dice][remainder] = subans
        return int(subans)
