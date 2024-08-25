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
        
        prev = None
        
        curr = root
        
        while curr or stk:
            if curr:
                stk.append(curr)
                curr = curr.left
            else:
                curr = stk[-1]
                
                # right subtree not present or was already seen
                if not curr.right or curr.right == prev:
                    ans.append(curr.val)
                    stk.pop()
                    prev = curr
                    curr = None
                else:
                    curr = curr.right
        
        return ans
