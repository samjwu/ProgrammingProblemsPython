class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        rowMin = [1e5+1 for i in range(m)]
        colMax = [-1 for j in range(n)]
        
        for i in range(m):
            for j in range(n):
                rowMin[i] = min(rowMin[i], matrix[i][j])
                colMax[j] = max(colMax[j], matrix[i][j])
                
        ans = []
        
        for row in rowMin:
            if row in colMax:
                ans.append(row)
                
        return ans
