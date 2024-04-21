class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = [[] for i in range(n)]
        
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])
        
        seen = set()
        
        q = deque()
        
        q.append(source)
        
        while q:
            vertex = q.popleft()
            
            if vertex == destination:
                return True
            
            for neighbor in neighbors[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append(neighbor)
                    
        return False
