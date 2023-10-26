class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        
        memo = {}
        
        arr.sort()
        
        for x in arr:
            memo[x] = 1
            
            for y in memo:
                if x % y == 0:
                    # number of new trees that use 
                    # y as the left subtree and quotient as right subtree = 
                    # product of number of trees with y as root
                    # and number of trees with quotient as root

                    # note: as y iterates over all in memo, we also count swap
                    # with y as right subtree and quotient as left subtree
                    memo[x] = (memo[x] + memo[y] * memo.get(x/y, 0)) % mod
            
        return sum(memo.values()) % mod
