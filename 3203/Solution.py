class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n = len(edges1) + 1
        m = len(edges2) + 1

        # build graphs
        graph1 = self.buildGraph(n, edges1)
        graph2 = self.buildGraph(m, edges2)

        # calc diameters
        diameter1 = self.calcDiameter(n, graph1)
        diameter2 = self.calcDiameter(m, graph2)

        # combine center of each tree
        # result is half of each diameter, plus 1 new edge
        combinedDiameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        # Return the maximum of the three possibilities
        return max(diameter1, diameter2, combinedDiameter)

    def buildGraph(self, size, edges):
        graph = [[] for i in range(size)]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        return graph

    def calcDiameter(self, n, graph):
        # use bfs to find farthest node from 0th node
        # this is one endpoint of the diameter
        endpoint1, someDist = self.bfs(n, graph, 0)

        # use bfs to find farthest node from endpoint 1
        # this yields second endpoint and the diameter
        endpoint2, diameter = self.bfs(n, graph, endpoint1)

        return diameter

    def bfs(self, n, graph, src):
        q = deque([src])

        visited = [False] * n
        visited[src] = True

        dist = 0
        node = src

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                node = curr

                for neighbor in graph[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append(neighbor)

            if q:
                dist += 1

        return node, dist
