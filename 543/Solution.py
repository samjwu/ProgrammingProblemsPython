# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        self.dfs(root)
        
        return self.ans
    
    def dfs(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        
        self.ans = max(self.ans, l + r)
        
        return max(l, r) + 1
