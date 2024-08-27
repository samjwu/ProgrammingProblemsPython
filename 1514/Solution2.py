class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)

        for i, (u, v) in enumerate(edges):
            graph[u].append([v, succProb[i]])
            graph[v].append([u, succProb[i]])
            
        dist = [0 for i in range(n)]
        dist[start] = 1
        
        q = deque([start])

        while q:
            node = q.popleft()
            
            for neighbor, prob in graph[node]:
                if dist[node] * prob > dist[neighbor]:
                    dist[neighbor] = dist[node] * prob
                    q.append(neighbor)
                    
        return dist[end]
