# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        lo = root.val
        hi = root.val
        
        return self.dfs(root, lo, hi)
    
    def dfs(self, root: Optional[TreeNode], lo: int, hi: int) -> int:
        if root is None:
            return hi - lo
        
        lo = min(lo, root.val)
        hi = max(hi, root.val)
        
        l = self.dfs(root.left, lo, hi)
        r = self.dfs(root.right, lo, hi)
        
        return max(l, r)
