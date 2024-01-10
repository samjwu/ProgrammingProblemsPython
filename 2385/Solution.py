# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        graph = {}
        self.buildGraph(root, 0, graph)

        seen = {start}
        q = deque([start])
        dist = 0

        while q:
            n = len(q)
            
            for i in range(n):
                node = q.popleft()
                
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        q.append(neighbor)
                        
            dist += 1

        return dist - 1

    def buildGraph(self, node: TreeNode, parent: int, graph: Dict[int, Set[int]]) -> None:
        if node is None:
            return
        
        if node.val not in graph:
            graph[node.val] = set()
            
        neighbors = graph[node.val]
        
        if parent != 0:
            neighbors.add(parent)
            
        if node.left:
            neighbors.add(node.left.val)
            
        if node.right:
            neighbors.add(node.right.val)
            
        self.buildGraph(node.left, node.val, graph)
        self.buildGraph(node.right, node.val, graph)
