# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        stk = []
        curr = root
        lastVisitedRightNode = None

        while stk or curr:
            # traverse to leftmost node
            while curr:
                stk.append(curr)
                curr = curr.left

            # visit a left node
            curr = stk[-1]

            # go to unvisited right subtree
            if curr.right and curr.right is not lastVisitedRightNode:
                curr = curr.right
                continue

            # discard visited left node
            stk.pop()

            if not curr.right and not curr.left and curr.val == target:
                # edge case: root is leaf node with value target
                if not stk:
                    return None

                parent = stk[-1]

                if parent.left is curr:
                    parent.left = None
                elif parent.right is curr:
                    parent.right = None

            # mark right node visited
            lastVisitedRightNode = curr
            
            # discard visited right node
            curr = None

        return root
