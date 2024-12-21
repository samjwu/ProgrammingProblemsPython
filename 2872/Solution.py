class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # build graph
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.ans = 0

        # dfs from 0th node
        self.dfs(0, -1, graph, values, k)

        return self.ans

    def dfs(self, curr: int, parent: int, graph: List[List[int]], values: List[int], k: int) -> int:
        # sum of tree is sum of all subtrees plus root value
        treeSum = 0

        # add sum of subtrees
        # dfs on neighbors via edges
        for neighbor in graph[curr]:
            # avoid revisiting from source (parent) node
            if neighbor != parent:
                treeSum += self.dfs(neighbor, curr, graph, values, k)
                # modulo for large values
                # works since sum just needs to be divisible by k
                treeSum %= k

        # add root value
        treeSum += values[curr]
        treeSum %= k

        # if current tree sum is divisible by k
        # break the edge to its parent, adding 1 valid component
        if treeSum == 0:
            self.ans += 1

        return treeSum
