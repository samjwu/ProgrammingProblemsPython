# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        stk = []
        
        curr = root
        
        while curr or stk:
            if curr:
                ans.append(curr.val)
                stk.append(curr)
                curr = curr.right
            else:
                curr = stk.pop()
                curr = curr.left
        
        # preorder is root, left, right
        # ans is root, right, left
        # ans reversed is left, right, root
        # postorder is left, right, root
        ans.reverse()
        
        return ans
