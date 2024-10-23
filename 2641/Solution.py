# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])

        levelSums = []

        # calc sum of nodes at each level
        while q:
            n = len(q)
            levelSum = 0

            for i in range(n):
                node = q.popleft()
                levelSum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            levelSums.append(levelSum)

        # update nodes to cousin sums
        q.append(root)
        # root has no cousins
        root.val = 0
        level = 1

        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()

                # cousin sum is level sum minus node val
                # and any other child val of the same parent
                childSum = 0
                if node.left:
                    childSum += node.left.val
                if node.right:
                    childSum += node.right.val

                if node.left:
                    node.left.val = levelSums[level] - childSum
                    q.append(node.left)
                if node.right:
                    node.right.val = levelSums[level] - childSum
                    q.append(node.right)
                    
            level += 1

        return root
