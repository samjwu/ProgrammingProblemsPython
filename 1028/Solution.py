# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.index = 0

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        return self.traverse(traversal, 0)

    def traverse(self, traversal, depth):
        # reached end of string
        if self.index >= len(traversal):
            return None

        # count dashes
        dashes = 0
        while self.index + dashes < len(traversal) and traversal[self.index + dashes] == "-":
            dashes += 1

        # early exit if dashes don't match current depth
        # since current node is right subtree of previous node
        if dashes != depth:
            return None

        # update position after counting dashes
        self.index += dashes

        # determine value
        value = 0
        while self.index < len(traversal) and traversal[self.index].isdigit():
            value = value * 10 + int(traversal[self.index])
            self.index += 1

        # create node from value
        node = TreeNode(value)

        # recurse to build left and right subtrees
        node.left = self.traverse(traversal, depth + 1)
        node.right = self.traverse(traversal, depth + 1)

        return node
