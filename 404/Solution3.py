# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        q = deque()
        q.append((root, False))
        
        while q:
            curr, isLeft = q.popleft()
            
            if curr.left is None and curr.right is None and isLeft:
                ans += curr.val
                
            if curr.right:
                q.append((curr.right, False))
                
            if curr.left:
                q.append((curr.left, True))
                
        return ans
