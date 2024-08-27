class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        m = len(edges)

        dist = [0 for i in range(n)]
        dist[start] = 1
        
        for i in range(n - 1):
            updated = False

            for j in range(m):
                u, v = edges[j]

                prob = succProb[j]
                
                if dist[u] * prob > dist[v]:
                    dist[v] = dist[u] * prob
                    updated = True
                    
                if dist[v] * prob > dist[u]:
                    dist[u] = dist[v] * prob
                    updated = True

            # stop iterating if there is no longer path with a higher probability
            # since the answer has been found
            if not updated:
                break
        
        return dist[end]
