# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        self.prev = defaultdict(list)
        
        self.ans = True
        
        self.dfs(root, 0)
        
        return self.ans
    
    def dfs(self, node: Optional[TreeNode], depth: int) -> bool:
        if node is None:
            return True
        
        if depth % 2 == 0:
            if node.val % 2 == 0:
                self.ans = False
        else:
            if node.val % 2 == 1:
                self.ans = False
                
        if len(self.prev[depth]) != 0:
            if depth % 2 == 0:
                if self.prev[depth][-1] >= node.val:
                    self.ans = False
            else:
                if self.prev[depth][-1] <= node.val:
                    self.ans = False
                    
        self.prev[depth].append(node.val)
                
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)
