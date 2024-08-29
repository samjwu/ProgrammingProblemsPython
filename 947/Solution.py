class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)

        graph = [[] for i in range(n)]

        # connect stones on the same x or y
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)

        numConnected = 0
        
        visited = [False for i in range(n)]

        def dfs(stone: int):
            visited[stone] = True

            for neighbor in graph[stone]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                numConnected += 1

        return n - numConnected
