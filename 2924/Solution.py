class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0 for i in range(n)]
        
        for edge in edges:
            indegree[edge[1]] += 1
        
        champ = -1
        
        for i in range(n):
            if indegree[i] == 0:
                if champ != -1:
                    return -1
                champ = i
                
        return champ
