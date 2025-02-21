from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        self.bfs(root)

    def find(self, target: int) -> bool:
        return target in self.seen

    def bfs(self, node: Optional[TreeNode]) -> None:
        if not node:
            return

        node.val = 0

        q = deque()
        q.append(node)

        while q:
            curr = q.popleft()
            self.seen.add(curr.val)

            if curr.left:
                curr.left.val = curr.val*2 + 1
                q.append(curr.left)

            if curr.right:
                curr.right.val = curr.val*2 +2
                q.append(curr.right)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
