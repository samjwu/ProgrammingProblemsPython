class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m = len(land)
        n = len(land[0])
        
        visited = [[False for j in range(n)] for i in range(m)]
        
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        ans = []
        
        def dfs(land: List[List[int]], x: int, y: int, bottomCorner: List[int]) -> None:
            visited[x][y] = True
            
            bottomCorner[0] = max(bottomCorner[0], x)
            bottomCorner[1] = max(bottomCorner[1], y)
            
            for direction in directions:
                nextX = x + direction[0]
                nextY = y + direction[1]
                
                if nextX >= 0 and nextX < m and nextY >= 0 and nextY < n and visited[nextX][nextY] == False and land[nextX][nextY] == True:
                    dfs(land, nextX, nextY, bottomCorner)
        
        for r1 in range(m):
            for c1 in range(n):
                if visited[r1][c1] == False and land[r1][c1] == True:
                    bottomCorner = [0, 0]
                    
                    dfs(land, r1, c1, bottomCorner)
                    
                    ans.append([r1, c1, bottomCorner[0], bottomCorner[1]])
        
        return ans
