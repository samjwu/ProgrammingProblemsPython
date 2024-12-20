# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = [root]

        level = 0

        while q:
            n = len(q)
            curr = []

            for i in range(n):
                node = q.pop(0)
                curr.append(node)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level % 2 == 1:
                left = 0
                right = len(curr) - 1

                while left < right:
                    tmp = curr[left].val
                    curr[left].val = curr[right].val
                    curr[right].val = tmp
                    
                    left += 1
                    right -= 1

            level += 1

        return root
