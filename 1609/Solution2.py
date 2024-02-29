from queue import Queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = Queue()
        
        q.put(root)
        
        level = 0
        
        while q.qsize() > 0:
            n = q.qsize()
            
            prev = -1
            
            for i in range(n):
                node = q.get()
                
                if level % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                    elif prev != -1 and prev >= node.val:
                        return False
                else:
                    if node.val % 2 == 1:
                        return False
                    elif prev != -1 and prev <= node.val:
                        return False
                
                if node.left is not None:
                    q.put(node.left)
                    
                if node.right is not None:
                    q.put(node.right)
                
                prev = node.val
                
            level += 1            
        
        return True
