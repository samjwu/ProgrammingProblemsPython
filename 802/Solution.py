class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        visited = [False] * n
        in_path = [False] * n

        for i in range(n):
            self.is_in_cycle(i, graph, visited, in_path)

        ans = []
        for i in range(n):
            if not in_path[i]:
                ans.append(i)

        return ans

    # dfs
    def is_in_cycle(self, node, graph, visited, in_path):
        if in_path[node]:
            return True

        if visited[node]:
            return False

        visited[node] = True
        in_path[node] = True

        for neighbor in graph[node]:
            if self.is_in_cycle(neighbor, graph, visited, in_path):
                return True
        
        in_path[node] = False
        return False
