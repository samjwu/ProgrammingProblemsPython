class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]

        # construct reversed DAG
        for edge in edges:
            graph[edge[1]].append(edge[0])

        ans = []

        for curr in range(n):
            subans = []
            visited = set()
            self.dfs(curr, graph, visited)
            
            for node in range(n):
                if node == curr:
                    continue

                if node in visited:
                    subans.append(node)

            ans.append(subans)

        return ans

    def dfs(self, curr: int, graph: List[List[int]], visited: List[int]):
        visited.add(curr)
        
        for neighbour in graph[curr]:
            if neighbour not in visited:
                self.dfs(neighbour, graph, visited)
