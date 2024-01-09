# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = []
        leaves2 = []
        
        def getLeaves(root: Optional[TreeNode], leaves: List[TreeNode]) -> None:
            if root is None:
                return
            
            getLeaves(root.left, leaves)
            
            if root.left is None and root.right is None:
                leaves.append(root.val)
            
            getLeaves(root.right, leaves)
        
        getLeaves(root1, leaves1)
        getLeaves(root2, leaves2)
        
        return leaves1 == leaves2
