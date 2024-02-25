class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = [i for i in range(n)]
        self.groupSize = [1 for i in range(n)]
        
    def find(self, x: int) -> int:
        if x == self.parents[x]:
            return x
        
        # path compression
        self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]
    
    def unify(self, x: int, y: int) -> None:
        parentX = self.find(x)
        parentY = self.find(y)
        
        if parentX == parentY:
            return
        
        # swap to ensure group y is always larger
        # then always unify under group y
        if self.groupSize[parentX] > self.groupSize[parentY]:
            parentX, parentY = parentY, parentX
            
        self.groupSize[parentY] += self.groupSize[parentX]
        
        self.parents[parentX] = parentY
    
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
 
        # unifyNext[x] = index of a value in nums with x as its gcd
        # used to track the next number to unify
        unifyNext = [-1 for i in range(max(nums) + 1)]
        
        uf = UnionFind(n)
        
        for i in range(n):
            quotient = nums[i]
            
            for factor in range(2, nums[i]):
                # skip if factor is greater than sqrt of nums[i]
                # since smaller factors are already tried earlier
                if factor * factor > nums[i]:
                    break
                    
                if nums[i] % factor != 0:
                    continue
                
                # unify the current number with the previous one
                if unifyNext[factor] != -1:
                    uf.unify(unifyNext[factor], i)
                # otherwise there is no number to unify,
                # so set it as the current one
                else:
                    unifyNext[factor] = i
                
                # get quotient of
                # nums[i] divided by its GCD
                while quotient % factor == 0:
                    quotient //= factor
                    
            # unify quotient and GCD if it's not 1
            if quotient > 1:
                if unifyNext[quotient] != -1: 
                    uf.unify(unifyNext[quotient], i)
                else:
                    unifyNext[quotient] = i
                    
        return uf.groupSize[uf.find(0)] == n
