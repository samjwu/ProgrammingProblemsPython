# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        return self.build_tree(0, n-1, 0, preorder, postorder)

    def build_tree(self, pre_start: int, pre_end: int, post_start: int, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # base case: no nodes
        if pre_start > pre_end:
            return None

        # base case: exactly 1 node
        if pre_start == pre_end:
            return TreeNode(preorder[pre_start])

        # in preorder, element after root is left child
        left = preorder[pre_start + 1]

        # determine number of nodes in left subtree
        # by counting number of nodes between postorder start and left node in postorder
        left_count = 1
        while postorder[post_start + left_count - 1] != left:
            left_count += 1

        root = TreeNode(preorder[pre_start])

        # recurse to build left subtree
        root.left = self.build_tree(
            pre_start + 1,
            pre_start + left_count,
            post_start,
            preorder,
            postorder
        )

        # recurse to build right subtree
        root.right = self.build_tree(
            pre_start + left_count + 1,
            pre_end,
            post_start + left_count,
            preorder,
            postorder
        )

        return root
