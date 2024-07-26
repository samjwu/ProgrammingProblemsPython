class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for i in range(n)]

        # dists[i][j] = shortest dist from city i to city j
        dists = [[float("inf")] * n for i in range(n)]

        for i in range(n):
            # city dist to itself is 0
            dists[i][i] = 0

        for start, end, weight in edges:
            graph[start].append((end, weight))
            graph[end].append((start, weight))

        for i in range(n):
            self.dijkstra(n, graph, dists[i], i)

        return self.calcFewestReachable(n, dists, distanceThreshold)

    def dijkstra(self, n: int, graph: List[List[tuple]], dist: List[int], start: int) -> None:
        # (dist, city)
        minHeap = [(0, start)]

        # dist[i] = shortest dist from start city to ith city
        dist[:] = [float("inf") for i in range(n)]

        dist[start] = 0

        while minHeap:
            currDist, currCity = heapq.heappop(minHeap)

            # path is longer than already stored one
            if currDist > dist[currCity]:
                continue

            for neighbor, weight in graph[currCity]:
                # found new shorter path
                if (dist[neighbor] > currDist + weight):
                    dist[neighbor] = (currDist + weight)
                    heapq.heappush(minHeap, (dist[neighbor], neighbor))

    def calcFewestReachable(self, n: int, dists: List[List[int]], distance_threshold: int) -> int:
        ans = -1
        fewestReachable = n

        for i in range(n):
            reachable = sum(1 for j in range(n) if i != j and dists[i][j] <= distance_threshold)

            if reachable <= fewestReachable:
                fewestReachable = reachable
                ans = i

        return ans
