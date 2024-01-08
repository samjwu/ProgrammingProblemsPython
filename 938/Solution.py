# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        
        def traverse(root: Optional[TreeNode]) -> None:
            if root is None:
                return
        
            if root.val >= low and root.val <= high:
                self.ans += root.val
                
            traverse(root.left)
            traverse(root.right)
            
        traverse(root)
        
        return self.ans
