# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        remove = set(to_delete)

        ans = []

        root = self.traverse(root, remove, ans)

        if root:
            ans.append(root)

        return ans

    def traverse(self, node: TreeNode, remove: Set[int], ans: List[TreeNode]) -> TreeNode:
        """
        Use postorder traversal to avoid deleting nodes too early
        (ie: before we can visit them)
        """
        if not node:
            return None

        node.left = self.traverse(node.left, remove, ans)
        node.right = self.traverse(node.right, remove, ans)

        if node.val in remove:
            if node.left:
                ans.append(node.left)
            if node.right:
                ans.append(node.right)
            return None

        return node
