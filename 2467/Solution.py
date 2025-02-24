class Solution:
    def __init__(self):
        self.bob_path = {}
        self.visited = []
        self.tree = []

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        ans = float("-inf")
        self.tree = [[] for _ in range(n)]
        self.bob_path = {}
        self.visited = [False] * n
        q = deque([(0, 0, 0)])

        # build tree
        for edge in edges:
            self.tree[edge[0]].append(edge[1])
            self.tree[edge[1]].append(edge[0])

        # determine bob path
        self.dfs(bob, 0)

        # bfs
        self.visited = [False] * n
        while q:
            src, time, income = q.popleft()

            # alice visits node before pop
            if src not in self.bob_path or time < self.bob_path[src]:
                income += amount[src]
            
            # both visit node at same time
            elif time == self.bob_path[src]:
                income += amount[src] // 2

            # if node is leaf that was not starting node 0,
            # compare to current answer
            if len(self.tree[src]) == 1 and src != 0:
                ans = max(ans, income)

            # visit neighbors
            for neighbor in self.tree[src]:
                if not self.visited[neighbor]:
                    q.append((neighbor, time + 1, income))

            # marked visited
            self.visited[src] = True

        return ans

    def dfs(self, src: int, time: int):
        # mark visited, set time bob reached node
        self.visited[src] = True
        self.bob_path[src] = time

        # found dest node 0
        if src == 0:
            return True

        # visit neighbors
        for neighbor in self.tree[src]:
            if not self.visited[neighbor]:
                if self.dfs(neighbor, time + 1):
                    return True

        # to ignore nodes in bob's path that do not reach dest node 0,
        # pop nodes from path if 0 is not visited
        self.bob_path.pop(src, None)
        return False
