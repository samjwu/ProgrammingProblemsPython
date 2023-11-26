class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        ans = 0

        for row in range(m):
            for col in range(n):
                # count streak of ones in current col, top down
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]

            # sorting rows equivalent to rearranging cols
            ones_streak = sorted(matrix[row], reverse=True)
            
            for i in range(n):
                # ones_streak[i] is vertical height of rectangle
                # i+1 is horizontal length of rectangle
                ans = max(ans, ones_streak[i] * (i + 1))

        return ans
