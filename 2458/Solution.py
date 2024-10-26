# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # memoize heights of seen nodes
        memo = {}

        # store max height if subtree at a given node is removed
        # excluding the root node
        ans = {}

        def calcHeight(node: Optional[TreeNode]) -> int:
            if not node:
                return -1

            if node in memo:
                return memo[node]

            height = max(calcHeight(node.left), calcHeight(node.right)) + 1

            memo[node] = height
            return height

        def dfs(node: Optional[TreeNode], height: int, maxHeight: int):
            if not node:
                return

            # store max height seen so far at current node
            ans[node.val] = maxHeight

            # when traversing left and right subtrees,
            # include max height of sibling subtree
            # since pruning current node removes height of both subtrees

            dfs(
                node.left,
                height + 1,
                max(maxHeight, height + 1 + calcHeight(node.right)),
            )

            dfs(
                node.right,
                height + 1,
                max(maxHeight, height + 1 + calcHeight(node.left)),
            )

        dfs(root, 0, 0)

        return [ans[q] for q in queries]
