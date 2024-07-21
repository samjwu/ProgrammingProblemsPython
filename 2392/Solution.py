class Solution:
    def buildMatrix(
        self,
        k: int,
        rowConditions: List[List[int]],
        colConditions: List[List[int]],
    ) -> List[List[int]]:
        rows = self.topologicalSort(rowConditions, k)
        cols = self.topologicalSort(colConditions, k)

        # if no topological sort exists, there is no valid answer
        if not rows or not cols:
            return []

        ans = [[0 for j in range(k)] for i in range(k)]

        # store position index of each value number
        rowPosition = {num: i for i, num in enumerate(rows)}
        colPosition = {num: i for i, num in enumerate(cols)}

        for num in range(1, k+1):
            if num in rowPosition and num in colPosition:
                ans[rowPosition[num]][colPosition[num]] = num

        return ans

    def topologicalSort(self, edges: List[List[int]], n: int) -> List[int]:
        # construct adjacency list
        graph = defaultdict(list)

        order = []

        visited = [0 for i in range(n+1)]

        cycle = [False]

        for x, y in edges:
            graph[x].append(y)
        
        for i in range(1, n+1):
            if visited[i] == 0:
                self.dfs(i, graph, visited, order, cycle)
                
                # if there is a cycle, there is no valid answer
                if cycle[0]:
                    return []

        # reverse path after dfs to get topological order
        order.reverse()
        return order

    def dfs(
        self,
        node: int,
        graph: defaultdict,
        visited: List[int],
        order: List[int],
        cycle: List[bool],
    ):
        # currently being visited
        visited[node] = 1
        
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                self.dfs(neighbor, graph, visited, order, cycle)
                
                # if there is a cycle, there is no valid answer
                if cycle[0]:
                    return
            elif visited[neighbor] == 1:
                # found self cycle
                cycle[0] = True
                return
        
        # was visited
        visited[node] = 2
        
        order.append(node)
