class Solution:
    def calcLargestSquare(self, matrix: List[List[int]], memo: List[List[int]], x: int, y: int) -> int:
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return 0
        
        if matrix[x][y] == 0:
            return 0
        
        if memo[x][y] != -1:
            return memo[x][y]
        
        side = self.calcLargestSquare(matrix, memo, x+1, y)
        bottom = self.calcLargestSquare(matrix, memo, x, y+1)
        diag = self.calcLargestSquare(matrix, memo, x+1, y+1)
        
        memo[x][y] = 1 + min(side, bottom, diag)
        return memo[x][y]
        
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        memo = [[-1 for j in range(n)] for i in range(m)]
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                # largest square at index also has same number of subsquares
                # as the size of its side
                ans += self.calcLargestSquare(matrix, memo, i, j)
                
        return ans
