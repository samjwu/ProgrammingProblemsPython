# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])

        ans = 0

        # level order traversal
        while q:
            n = len(q)
            level = []

            for i in range(n):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans += self.calcSwaps(level)

        return ans

    def calcSwaps(self, arr: list) -> int:
        swaps = 0

        target = sorted(arr)

        # track index of values for swaps
        pos = {val: idx for idx, val in enumerate(arr)}

        # swap until arr matches sorted target
        for i in range(len(arr)):
            if arr[i] != target[i]:
                swaps += 1

                # simulate swap
                # get current position of ideal value
                curr = pos[target[i]]
                # update current position of value at current index in position dict
                pos[arr[i]] = curr
                # update current position of value at current index in array
                arr[curr] = arr[i]

        return swaps
