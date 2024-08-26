"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        
        if not root:
            return ans

        # store (node, are the node's children visited)
        stk = [(root, False)]

        while stk:
            node, hasVisitedChildren = stk.pop()

            # for postorder traversal
            # add the node value after its children are visited
            if hasVisitedChildren:
                ans.append(node.val)
            else:
                stk.append((node, True))

                for child in reversed(node.children):
                    stk.append((child, False))

        return ans
