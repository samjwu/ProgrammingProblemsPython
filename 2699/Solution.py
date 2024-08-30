class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        self.MAXWEIGHT = int(2e9)

        # graph[src] = list of pairs (dest, weight)
        graph = [[] for i in range(n)]

        for u, v, w in edges:
            if w != -1:
                graph[u].append((v, w))
                graph[v].append((u, w))

        minDist = self.dijkstra(graph, source, destination)

        if minDist < target:
            return []

        if minDist == target:
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = self.MAXWEIGHT

            return edges

        # current answer does not meet target
        # try adjusting edges to hit the target
        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                continue

            # use min init weight of 1
            # then calc needed increase to hit target
            edges[i][2] = 1
            graph[u].append((v, 1))
            graph[v].append((u, 1))

            # calc new dist with custom weight
            newDist = self.dijkstra(graph, source, destination)

            if newDist <= target:
                edges[i][2] += target - newDist

                for j in range(i + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = self.MAXWEIGHT

                return edges

        return []

    def dijkstra(self, graph: List[List[Tuple[int, int]]], src: int, destination: int) -> int:
        dists = [self.MAXWEIGHT for i in range(len(graph))]

        dists[src] = 0

        # hold (dist, node)
        minHeap = [(0, src)]

        while minHeap:
            d, u = heapq.heappop(minHeap)

            if d > dists[u]:
                continue

            for v, w in graph[u]:
                if d + w < dists[v]:
                    dists[v] = d + w
                    heapq.heappush(minHeap, (dists[v], v))

        return dists[destination]
