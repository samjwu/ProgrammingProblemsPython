class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        freq = defaultdict(int)
        
        n = len(grid)
        
        for i in range(n):
            for j in range(n):
                freq[grid[i][j]] += 1
                
        ans = [-1, -1]
        
        for i in range(1, n**2 + 1):
            if freq[i] == 2:
                ans[0] = i
            elif freq[i] == 0:
                ans[1] = i
                
        return ans
