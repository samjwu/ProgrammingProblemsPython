# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        stk = []
        index = 0
        root = None

        while index < n:
            # count dashes
            depth = 0
            while index < n and traversal[index] == "-":
                depth += 1
                index += 1

            # determine value
            value = 0
            while index < n and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1

            # create node from value
            node = TreeNode(value)

            # depth 0 is root
            if depth == 0:
                root = node
            else:
                # pop nodes from stack
                # until top node has less depth than current node
                while len(stk) > depth:
                    stk.pop()

                # set current node as left subtree of top node on stack
                # otherwise right subtree if left already exists
                if stk[-1].left == None:
                    stk[-1].left = node
                else:
                    stk[-1].right = node

            # push node to stack
            stk.append(node)

        return root
