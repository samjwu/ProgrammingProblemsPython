class Solution:
    cycle_start = -1

    def dfs(self, src, visited, graph, parent):
        visited[src] = True

        for neighbor in graph[src]:
            if not visited[neighbor]:
                parent[neighbor] = src
                self.dfs(neighbor, visited, graph, parent)
            elif neighbor != parent[src] and self.cycle_start == -1:
                # if node was visited and parent is different
                # then it is start of cycle
                self.cycle_start = neighbor
                parent[neighbor] = src

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        visited = [False] * n
        parent = [-1] * n

        graph = [[] for i in range(n)]
        for edge in edges:
            graph[edge[0] - 1].append(edge[1] - 1)
            graph[edge[1] - 1].append(edge[0] - 1)

        self.dfs(0, visited, graph, parent)

        # backtrack from start of cycle
        # mark all nodes in cycle
        cycle_nodes = {}
        node = self.cycle_start
        while True:
            cycle_nodes[node] = 1
            node = parent[node]
            if node == self.cycle_start:
                break

        # remove edge if both nodes are cycle nodes
        for i in range(n - 1, -1, -1):
            if (edges[i][0] - 1) in cycle_nodes and (edges[i][1] - 1) in cycle_nodes:
                return edges[i]

        return []
