# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        graph = {}

        leaves = set()

        self.traverse(root, None, graph, leaves)

        ans = 0

        for leaf in leaves:
            q = []
            q.append(leaf)

            seen = set()
            seen.add(leaf)
            
            # bfs from every leaf
            for i in range(distance + 1):
                n = len(q)
                for j in range(n):
                    curr = q.pop(0)

                    # there is a path to another leaf with length <= distance
                    if curr in leaves and curr != leaf:
                        ans += 1

                    if curr in graph:
                        for neighbor in graph.get(curr):
                            if neighbor not in seen:
                                q.append(neighbor)
                                seen.add(neighbor)

        # divide by 2 to avoid double counting
        return ans // 2
    
    def traverse(self, curr: TreeNode, prev: TreeNode, graph: dict[TreeNode, list[TreeNode]], leaves: set[TreeNode]) -> None:
        if curr is None:
            return

        if curr.left is None and curr.right is None:
            leaves.add(curr)

        if prev is not None:
            if prev not in graph:
                graph[prev] = []
            graph[prev].append(curr)

            if curr not in graph:
                graph[curr] = []
            graph[curr].append(prev)

        self.traverse(curr.left, curr, graph, leaves)
        self.traverse(curr.right, curr, graph, leaves)
