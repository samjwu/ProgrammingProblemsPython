class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])

        # track row of max received points
        prev = points[0]

        for i in range(1, m):
            # calc max points received left to right
            left = [0 for i in range(n)]
            left[0] = prev[0]
            for j in range(1, n):
                left[j] = max(left[j - 1] - 1, prev[j])

            # calc max points received right to left
            right = [0 for i in range(n)]
            right[-1] = prev[-1]
            for j in range(n-2, -1, -1):
                right[j] = max(right[j + 1] - 1, prev[j])

            # calc max points received at current row
            curr = [0 for i in range(n)]
            for j in range(n):
                curr[j] = points[i][j] + max(left[j], right[j])

            prev = curr

        return max(prev)
