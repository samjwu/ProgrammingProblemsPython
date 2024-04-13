class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        # height[j] = number of consecutive 1s
        # in column j so far
        height = [0 for j in range(n)]

        # left[j] = index of the leftmost 1 in the row
        # with the element in column j so far
        left = [0 for j in range(n)]

        # right[j] = index of the rightmost 1 in the row
        # with the element in column j so far
        right = [n for j in range(n)]
        
        ans = 0
        
        for i in range(m):
            currLeft = 0
            currRight = n

            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    # reset height when matrix hits a 0
                    height[j] = 0
            
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], currLeft)
                else:
                    left[j] = 0
                    # set new current left to max when matrix hits a 0
                    currLeft = j+1
            
            for j in range(n-1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], currRight)
                else:
                    right[j] = n
                    # set new current right to min when matrix hits a 0
                    currRight = j
            
            for j in range(n):
                ans = max(ans, (right[j] - left[j]) * height[j])
        
        return ans
