# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        stk = []
        stk.append(root)

        ans = {}
        
        while stk:
            node = stk.pop()
            
            if not node.left and not node.right:
                ans[node] = node.val == 1
                continue
            
            if node.left in ans and node.right in ans:
                if node.val == 2:
                    ans[node] = ans[node.left] or ans[node.right]
                else:
                    ans[node] = ans[node.left] and ans[node.right]
            else:
                stk.append(node)

                if node.left:
                    stk.append(node.left)
                if node.right:
                    stk.append(node.right)
        
        return ans[root]
