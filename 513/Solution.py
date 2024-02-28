# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        self.maxDepth = -1
        
        self.dfs(root, 0)
        
        return self.ans

    def dfs(self, node: Optional[TreeNode], depth: int) -> None:
        if node is None:
            return
        
        if depth > self.maxDepth:
            self.maxDepth = depth
            self.ans = node.val

        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)
