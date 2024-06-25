# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        runningSum = 0
        stack = []
        node = root

        while len(stack) > 0 or node is not None:
            while node is not None:
                stack.append(node)
                node = node.right
                
            node = stack.pop()
            
            runningSum += node.val
            node.val = runningSum
            
            node = node.left
            
        return root
