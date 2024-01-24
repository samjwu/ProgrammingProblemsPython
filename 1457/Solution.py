# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node: Optional[TreeNode], seen: set[int]) -> None:
            if not node:
                return
            
            if node.val in seen:
                seen.remove(node.val)
            else:
                seen.add(node.val)
                
            if not node.left and not node.right:
                if len(seen) <= 1:
                    self.ans += 1
                    
            dfs(node.left, copy.copy(seen))
            dfs(node.right, copy.copy(seen))
               
        seen = set()
        dfs(root, seen)
        
        return self.ans
