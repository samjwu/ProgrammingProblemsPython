# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        stk = []
        node = root
        
        while node or stk:
            while node:
                stk.append(node)
                node = node.left
            
            node = stk.pop()
            
            ans.append(node.val)
            
            node = node.right
            
        return ans
