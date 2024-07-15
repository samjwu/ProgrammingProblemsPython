# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        parents = set()
        
        parentToChildren = {}
        
        for description in descriptions:
            parent, child, isLeft = description

            parents.add(parent)
            parents.add(child)
            
            children.add(child)

            if parent not in parentToChildren:
                parentToChildren[parent] = []

            parentToChildren[parent].append((child, isLeft))

        # root node is the one in parents but not in children
        for parent in parents.copy():
            if parent in children:
                parents.remove(parent)

        # parents set only contains root node now
        root = TreeNode(next(iter(parents)))

        queue = deque([root])

        while queue:
            parent = queue.popleft()
            
            for childValue, isLeft in parentToChildren.get(parent.val, []):
                child = TreeNode(childValue)
                queue.append(child)
                
                if isLeft == 1:
                    parent.left = child
                else:
                    parent.right = child

        return root
