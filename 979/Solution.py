# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return 0

            # coins exchanged with left subtree
            
            # positive = child gave coins to parents
            # negative = child took coins from parents
            exchangeLeft = dfs(node.left)
            
            # coins exchanged with right subtree
            exchangeRight = dfs(node.right)

            self.moves += abs(exchangeLeft) + abs(exchangeRight)

            # coins at node = node.val + exchangeLeft + exchangeRight

            # remove 1 to get the number of exchanges needed
            # to make number of coins at current node equal to 1
            return (node.val - 1) + exchangeLeft + exchangeRight

        dfs(root)

        return self.moves
