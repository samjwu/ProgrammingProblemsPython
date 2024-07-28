class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for i in range(n+1)]
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # store (dist, vertex)
        minHeap = [(0, 1)]

        dists = [[] for i in range(n+1)]
        dists[1].append(0)

        while minHeap:
            minDist, vertex = heapq.heappop(minHeap)

            if vertex == n and len(dists[n]) == 2:
                return max(dists[n])

            for neighbor in graph[vertex]:
                # green light
                if (minDist // change) % 2 == 0:
                    timeTaken = minDist + time
                else: # red light
                    wait = change - (minDist % change)
                    timeTaken = minDist + time + wait

                if len(dists[neighbor]) == 0 or (len(dists[neighbor]) == 1 and dists[neighbor] != [timeTaken]):
                    dists[neighbor].append(timeTaken)
                    heappush(minHeap, (timeTaken, neighbor))
