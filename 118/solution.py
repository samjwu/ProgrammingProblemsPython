from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return [[]]

        pascals_triangle = [[1]]
        
        for i in range(1, numRows):
            curr_row = [1]
            
            for j in range(len(pascals_triangle[i-1])-1):
                curr_row.append(pascals_triangle[i-1][j] + pascals_triangle[i-1][j+1])
            
            curr_row.append(1)
            pascals_triangle.append(curr_row)
            
        return pascals_triangle
