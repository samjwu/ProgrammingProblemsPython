class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        
        for u, v, w in flights:
            graph[u][v] = w
            
        # store triplet as (cost to reach, node, num stops)
        # set initial node as k+1 stops to visit neighbors
        minHeap = [(0, src, k+1)]
        
        # store cost to reach nodes
        visited = [0] * n
        
        while minHeap:
            cost, node, stops = heapq.heappop(minHeap)
            
            if node == dst:
                return cost
            
            # if node has been visited before with less steps
            # then skip current destination
            if visited[node] >= stops:
                continue
                
            visited[node] = stops
            
            for v, w in graph[node].items():
                heapq.heappush(minHeap, (cost + w, v, stops - 1))
                
        return -1
