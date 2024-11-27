import queue

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        graph = [[] for i in range(n)]

        for i in range(n-1):
            graph[i].append(i+1)

        for query in queries:
            u, v = query
            graph[u].append(v)
            ans.append(self.bfs(n, graph))

        return ans

    def bfs(self, n: int, graph: List[List[int]]) -> int:
        visited = [False for i in range(n)]
        visited[0] = True

        q = queue.Queue()
        q.put(0)

        pathLen = 0

        while q:
            level = q.qsize()

            for i in range(level):
                curr = q.get()

                if curr == n-1:
                    return pathLen

                for neighbor in graph[curr]:
                    if visited[neighbor]:
                        continue

                    q.put(neighbor)
                    
                    visited[neighbor] = True

            pathLen += 1

        return -1
