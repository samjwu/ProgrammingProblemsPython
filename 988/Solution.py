# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = ""

        self.dfs(root, "")

        return self.ans

    def dfs(self, node: Optional[TreeNode], curr: str) -> None:
        if not node:
            return

        curr = chr(node.val + ord("a")) + curr

        if not node.left and not node.right:
            if not self.ans or curr < self.ans:
                self.ans = curr

        if node.left:
            self.dfs(node.left, curr)
        
        if node.right:
            self.dfs(node.right, curr)
