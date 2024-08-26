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

        stk = [root]

        while stk:
            node = stk.pop()

            ans.append(node.val)

            for child in node.children:
                stk.append(child)

        ans.reverse()
        
        return ans
