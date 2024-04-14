# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        self.traverse(root, False)
        
        return self.ans
        
    def traverse(self, root: Optional[TreeNode], isLeft: bool) -> None:
        if root is None:
            return
        
        if root.left is None and root.right is None and isLeft:
            self.ans += root.val
            
        self.traverse(root.left, True)
        self.traverse(root.right, False)
                