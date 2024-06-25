# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nums = []
        
        def buildNums(node: TreeNode) -> None:
            if node is None:
                return
            
            buildNums(node.left)
            nums.append(node.val)
            buildNums(node.right)
            
        buildNums(root)
        
        total = sum(nums)
        
        sums = [total]
        
        nodeMap = {nums[0]: sums[0]}
        
        for i in range(1, len(nums)):
            val = sums[i-1] - nums[i-1]
            sums.append(val)
            nodeMap[nums[i]] = val
            
        def buildGst(node: TreeNode) -> None:
            if node is None:
                return
            
            buildGst(node.left)
            node.val = nodeMap[node.val]
            buildGst(node.right)
            
        buildGst(root)
            
        return root
