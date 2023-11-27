class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        # knight_map[i] = number of reachable squares from ith square
        knight_map = [
            [4, 6], # 0
            [6, 8], # 1
            [7, 9], # 2
            [4, 8], # 3
            [3, 9, 0], # 4
            [], # 5
            [1, 7, 0], # 6
            [2, 6], # 7
            [1, 3], # 8
            [2, 4] # 9
        ]
        
        ans = 0
        
        # memoize via functools.cache decorator
        # return the number of solutions staring from ith square with n moves
        @cache
        def recurse(n: int, i: int) -> int:
            if n == 0:
                return 1
            
            subans = 0
            
            for ni in knight_map[i]:
                subans += recurse(n-1, ni)
                subans %= MOD
            
            return subans
        
        for i in range(10):
            ans += recurse(n-1, i)
            ans %= MOD
        
        return ans
