# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def traverse(root: Optional[TreeNode]) -> tuple[int, int]:
            if root is None:
                return (0, 0)
            
            (left_size, left_sum) = traverse(root.left)
            (right_size, right_sum) = traverse(root.right)
            
            total_size = left_size + right_size + 1
            total_sum = left_sum + right_sum + root.val
            
            if root.val == total_sum // total_size:
                self.ans += 1
            
            return (total_size, total_sum)
        
        traverse(root)
        return self.ans
