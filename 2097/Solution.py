class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(deque)
        outDegree = defaultdict(int)
        inDegree = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            outDegree[start] += 1
            inDegree[end] += 1

        path = []

        def dfs(node: int) -> None:
            while graph[node]:
                nextNode = graph[node].popleft()
                dfs(nextNode)
            path.append(node)

        # for a unique path,
        # starting node has an indegree smaller than its outdegree by exactly 1
        # since it begins the path
        startNode = -1
        for node in outDegree:
            if outDegree[node] == inDegree[node] + 1:
                startNode = node
                break

        # otherwise path is circular, so arbitrarily pick first pair
        if startNode == -1:
            startNode = pairs[0][0]

        dfs(startNode)
        
        # dfs returns path in reverse
        path.reverse()

        ans = []
        for i in range(1, len(path)):
            ans.append([path[i-1], path[i]])

        return ans
