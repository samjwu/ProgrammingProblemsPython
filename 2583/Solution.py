# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        self.sums = []
        
        self.levelOrderTraversal(root)
        
        self.sums.sort()
        
        n = len(self.sums)
        
        if k > n:
            return -1
        
        return self.sums[n-k]
    
    def levelOrderTraversal(self, root: Optional[TreeNode]) -> None:
        q = deque()
        
        q.append(root)
        
        while q:
            n = len(q)
            levelSum = 0
            
            for i in range(n):
                node = q.popleft()
                levelSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            self.sums.append(levelSum)
            