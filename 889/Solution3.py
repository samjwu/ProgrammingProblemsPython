# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre_index = 0
        self.post_index = 0

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.build_tree(preorder, postorder)

    def build_tree(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Recursively visit nodes in preorder (root > left > right)
        So we can process preorder in the same order as we traverse

        Since postorder follows (left > right > root)
        A subtree is processed if the root is visited
        """
        # increment preorder, since we process the root for the current subtree
        root = TreeNode(preorder[self.pre_index])
        self.pre_index += 1

        # if postorder root was not visited, there is a left child
        # recurse to build left subtree
        if root.val != postorder[self.post_index]:
            root.left = self.build_tree(preorder, postorder)

        # if postorder root was not visited after previous recursion, there is a right child
        # recurse to build right subtree
        if root.val != postorder[self.post_index]:
            root.right = self.build_tree(preorder, postorder)

        # increment postorder, since we processed the subtree for current node
        self.post_index += 1
        return root
