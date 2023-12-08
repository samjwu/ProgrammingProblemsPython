# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        m = str(root.val)
        
        l = ""
        if root.left or root.right:
            l = "(" + self.tree2str(root.left) + ")"
            
        r = ""
        if root.right:
            r = "(" + self.tree2str(root.right) + ")"
        
        return f"{m}{l}{r}"
