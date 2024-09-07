# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        # try current tree, left subtree, right subtree
        return (self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right))

    def dfs(self, listNode: Optional[ListNode], treeNode: Optional[TreeNode]) -> bool:
        # reached end of list, found matching path in tree
        if not listNode:
            return True

        # list not completed
        if not treeNode:
            return False

        if treeNode.val != listNode.val:
            return False

        return self.dfs(listNode.next, treeNode.left) or self.dfs(listNode.next, treeNode.right)
