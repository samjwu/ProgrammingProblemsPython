class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        
        degree = [0 for i in range(n+1)]
        
        for edge in edges:
            degree[edge[0]] += 1
            degree[edge[1]] += 1
            
            if degree[edge[0]] > 1:
                return edge[0]
            
            if degree[edge[1]] > 1:
                return edge[1]
            
        return -1
