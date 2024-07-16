# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # map child value to its parent node
        parents = {}

        startNode = self.findStartNode(root, startValue)

        self.findParents(root, parents)

        q = deque([startNode])

        visited = set()

        visited.add(startNode)

        # reversedPath[nextNode] = (currentNode, direction)
        reversedPath = {}

        # bfs
        while q:
            curr = q.popleft()

            if curr.val == destValue:
                return self.generatePath(curr, reversedPath)

            # if current val has a parent
            # then it is a child, so go up
            if curr.val in parents:
                parent = parents[curr.val]

                if parent not in visited:
                    visited.add(parent)
                    q.append(parent)
                    reversedPath[parent] = (curr, "U")

            # traverse left child if not visited
            if (curr.left and curr.left not in visited):
                visited.add(curr.left)
                q.append(curr.left)
                reversedPath[curr.left] = (curr, "L")

            # traverse right child if not visited
            if (curr.right and curr.right not in visited):
                visited.add(curr.right)
                q.append(curr.right)
                reversedPath[curr.right] = (curr, "R")

        return ""

    def findStartNode(self, node: TreeNode, startValue: int) -> TreeNode:
        if not node:
            return None

        if node.val == startValue:
            return node

        leftSubtree = self.findStartNode(node.left, startValue)

        if leftSubtree:
            return leftSubtree

        return self.findStartNode(node.right, startValue)

    def findParents(self, node: TreeNode, parents: dict[int, TreeNode]) -> None:
        if not node:
            return

        if node.left:
            parents[node.left.val] = node
            self.findParents(node.left, parents)

        if node.right:
            parents[node.right.val] = node
            self.findParents(node.right, parents)
    
    def generatePath(self, node: TreeNode, reversedPath: dict[TreeNode, tuple[TreeNode, str]]) -> list[TreeNode]:
        path = []
        
        while node in reversedPath:
            path.append(reversedPath[node][1])
            node = reversedPath[node][0]

        path.reverse()
        
        return "".join(path)
