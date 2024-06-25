# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.runningSum = 0
        self.reverseTraverse(root)
        return root

    def reverseTraverse(self, node: TreeNode):
        if node is None:
            return

        self.reverseTraverse(node.right)
        self.runningSum += node.val
        node.val = self.runningSum
        self.reverseTraverse(node.left)
