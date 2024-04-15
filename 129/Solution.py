# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = None
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.traverse(root, 0)
        return self.ans
    
    def traverse(self, node: Optional[TreeNode], path: int):
        if node is None:
            return
        
        path *= 10
        path += node.val
        if node.left is None and node.right is None:
            self.ans += path
            return
        self.traverse(node.left, path)
        self.traverse(node.right, path)
