class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        def bfs(node):
            q = deque([(node, 1)])
            seen = {node: 1}
            level = 1

            while q:
                cur, level = q.popleft()

                for nei in graph[cur]:
                    if nei not in seen:
                        seen[nei] = level+1
                        q.append((nei, level+1))
                    elif seen[nei] == level:
                        # cycle with odd number of edges, invalid
                        return -1

            return level
        
        # build graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # store the largest number of groups in each connected component
        component_groups = []

        # find connected component for each node
        visited = set()
        for i in range(1, n+1):
            if i not in visited:
                # bfs to determine connected component
                q = deque([i])
                component = set()
                component.add(i)

                while q:
                    cur = q.popleft()
                    for nei in graph[cur]:
                        if nei not in component:
                            component.add(nei)
                            q.append((nei))
                            visited.add(nei)
                
                # bfs on each node, updating groups for current connected component
                component_groups.append(0)
                for i in component:
                    groups = bfs(i)
                    
                    if groups == -1:
                        return -1

                    component_groups[-1] = max(component_groups[-1], groups)

        return sum(component_groups)
