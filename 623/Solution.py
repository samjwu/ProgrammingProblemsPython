# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        
        q = deque()
        
        q.append(root)
        
        currDepth = 0
        
        while q:
            currDepth += 1
            
            n = len(q)
            
            for i in range(n):
                node = q.popleft()
                
                if currDepth == depth - 1:
                    oldLeft = node.left
                    newLeft = TreeNode(val)
                    node.left = newLeft
                    newLeft.left = oldLeft
                    
                    oldRight = node.right
                    newRight = TreeNode(val)
                    node.right = newRight
                    newRight.right = oldRight
                    
                    continue
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
            
        return root
