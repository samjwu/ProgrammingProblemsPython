class Solution:
    def preprocess(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        graph: dict[int, List[int]],
        is_prereq: List[List[bool]],
    ) -> None:
        # bfs
        for i in range(numCourses):
            q = deque([i])

            while q:
                node = q.popleft()

                for neighbor in graph.get(node, []):
                    # is_prereq doubles as a visited array
                    if not is_prereq[i][neighbor]:
                        is_prereq[i][neighbor] = True
                        q.append(neighbor)

    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        graph = {}
        for edge in prerequisites:
            if edge[0] not in graph:
                graph[edge[0]] = []
            graph[edge[0]].append(edge[1])

        # is_prereq[i][j] = True indicates j is a prereq of i
        # otherwise False
        is_prereq = [[False] * numCourses for i in range(numCourses)]
        self.preprocess(numCourses, prerequisites, graph, is_prereq)

        ans = []
        for query in queries:
            ans.append(is_prereq[query[0]][query[1]])

        return ans
