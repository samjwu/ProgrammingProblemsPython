class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        
        seen = [False for node in range(n)]
        
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def dfs(node: int) -> List[int]:
            if seen[node]:
                return []

            longestPath = []

            seen[node] = True

            for neighbor in graph[node]:
                if not seen[neighbor]:
                    path = dfs(neighbor)

                    if len(path) > len(longestPath):
                        longestPath = path

            longestPath += [node]
            
            seen[node] = False

            return longestPath

        path = dfs(0)
        node = path[0]

        longestPath = dfs(node)

        ans1 = longestPath[(len(longestPath)-1)//2]
        ans2 = longestPath[len(longestPath)//2]

        return set([ans1, ans2])
