class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        self.graph = defaultdict(list)
        self.ans = []
        
        for x, y in adjacentPairs:
            self.graph[x].append(y)
            self.graph[y].append(x)
        
        root = None
        for node in self.graph:
            if len(self.graph[node]) == 1:
                root = node
                break
        
        self.dfs(root, None)
        
        return self.ans
    
    def dfs(self, node: int, prev: int) -> None:
        self.ans.append(node)

        for neighbor in self.graph[node]:
            if neighbor != prev:
                self.dfs(neighbor, node)
