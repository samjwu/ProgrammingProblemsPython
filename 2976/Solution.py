class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # graph[src] = [(dest, cost to dest), ...]
        graph = [[] for i in range(26)]

        n = len(original)

        for i in range(n):
            src = ord(original[i]) - ord("a")
            dest = ord(changed[i]) - ord("a")
            graph[src].append((dest, cost[i]))

        minCosts = [self.dijkstra(i, graph) for i in range(26)]

        ans = 0

        for s, t in zip(source, target):
            if s != t:
                cost = minCosts[ord(s) - ord("a")][ord(t) - ord("a")]

                if cost == float("inf"):
                    return -1

                ans += cost

        return ans

    def dijkstra(self, start: int, graph: List[List[tuple]]) -> List[int]:
        minHeap = [(0, start)]

        minCosts = [float("inf") for i in range(26)]

        while minHeap:
            cost, char = heapq.heappop(minHeap)

            if minCosts[char] != float("inf"):
                continue

            minCosts[char] = cost

            for nextChar, nextCost in graph[char]:
                totalCost = cost + nextCost

                if minCosts[nextChar] == float("inf"):
                    heapq.heappush(minHeap, (totalCost, nextChar))

        return minCosts
