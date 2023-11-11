class Graph:
    
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for i in range(n)]

        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        src, dest, weight = edge

        self.graph[src].append((dest, weight))

    def shortestPath(self, node1: int, node2: int) -> int:
        n = len(self.graph)
        min_heap = [(0, node1)]

        nodeWeights = [inf] * (n)
        nodeWeights[node1] = 0

        while min_heap:
            curr_weight, curr_node = heappop(min_heap)

            if curr_weight > nodeWeights[curr_node]:
                continue

            if curr_node == node2:
                return curr_weight

            for neighbor, weight in self.graph[curr_node]:
                new_weight = curr_weight + weight
                
                if new_weight < nodeWeights[neighbor]:
                    nodeWeights[neighbor] = new_weight
                    heappush(min_heap, (new_weight, neighbor))

        return -1
    
    
    
# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
