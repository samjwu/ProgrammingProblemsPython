class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        
    def find(self, u: int) -> int:
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
            
        return self.parent[u]
    
    def union(self, u: int, v: int) -> bool:
        parentU = self.find(u)
        parentV = self.find(v)

        if parentU == parentV:
            return False

        if self.size[parentU] < self.size[parentV]:
            self.size[parentV] += self.size[parentU]
            self.parent[parentU] = parentV
        else:
            self.size[parentU] += self.size[parentV]
            self.parent[parentV] = parentU

        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [0, 1, 0, -1, 0]
        
        m = len(grid)
        n = len(grid[0])
        
        uf = UnionFind(m*n)
        
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue

                ans += 1

                for idx in range(4):
                    nextI = i + directions[idx]
                    nextJ = j + directions[idx+1]

                    if nextI < 0 or nextI == m or nextJ < 0 or nextJ == n or grid[nextI][nextJ] == "0":
                        continue

                    if uf.union(i * n + j, nextI * n + nextJ):
                        ans -= 1
                        
        return ans
