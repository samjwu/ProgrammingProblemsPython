class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        onesRow = [0 for i in range(m)]
        onesCol = [0 for i in range(n)]
        zeroesRow = [0 for i in range(m)]
        zeroesCol = [0 for i in range(n)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    onesRow[i] += 1
                    onesCol[j] += 1
                else:
                    zeroesRow[i] += 1
                    zeroesCol[j] += 1
                    
        diff = [[0 for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                diff[i][j] = onesRow[i] + onesCol[j] - zeroesRow[i] - zeroesCol[j]
        
        return diff
