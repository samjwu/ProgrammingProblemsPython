# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        
        def inorder(node: TreeNode) -> None:
            if node is None:
                return
            
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
            
        def buildTree(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            
            m = l + (r-l)//2
            
            node = TreeNode(nums[m])
            node.left = buildTree(l, m-1)
            node.right = buildTree(m+1, r)
            
            return node
        
        inorder(root)
        
        l = 0
        r = len(nums) - 1
        return buildTree(l, r)
