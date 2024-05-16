# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return root.val == 1

        leftSubtree = self.evaluateTree(root.left)
        rightSubtree = self.evaluateTree(root.right)
        
        if root.val == 2:
            return leftSubtree or rightSubtree
        else:
            return leftSubtree and rightSubtree
