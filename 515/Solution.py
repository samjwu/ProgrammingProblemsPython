# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        q = deque()
        
        if root:
            q.append(root)
        
        while q:
            n = len(q)
            hi = float("-inf")
            
            for i in range(n):
                node = q.popleft()
                hi = max(hi, node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ans.append(hi)
        
        return ans
