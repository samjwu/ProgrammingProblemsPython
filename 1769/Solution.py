class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)

        left = [0]*n
        balls = 0
        ops = 0

        for i in range(n):
            ops += balls

            left[i] = ops
            
            if boxes[i] == "1":
                balls += 1

        right = [0]*n
        balls = 0
        ops = 0

        for i in range(n-1, -1, -1):
            ops += balls

            right[i] = ops

            if boxes[i] == "1":
                balls += 1

        ans = []

        for i in range(n):
            ans.append(left[i] + right[i])

        return ans
