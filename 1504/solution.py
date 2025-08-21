from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        number_submatrices = 0
        
        # row[i][j] = number of consecutive 1s ending at mat[i][j]
        row = [[0 for j in range(n)] for i in range(m)]

        # preprocess matrix to find horizontal consecutive 1s
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    # saw 0, consecutive 1s ends
                    row[i][j] = 0
                else:
                    # saw 1, increment consecutive 1s
                    if j == 0:
                        row[i][j] = mat[i][j]
                    else:
                        row[i][j] = row[i][j-1] + 1

        # count submatrices with mat[i][j] as 1 for bottom right corner
        for i in range(m):
            for j in range(n):
                # get the most consecutive 1s for the current row
                curr = row[i][j]
                
                # move up to find bigger submatrices
                for k in range(i, -1, -1):
                    # most consecutive 1s is limited by the smallest row
                    curr = min(curr, row[k][j])
                    
                    # hit a row with no 1s, so stop looking
                    if curr == 0:
                        break
                    
                    # can make curr number of submatrices with mat[i][j] as 1 for bottom right corner
                    number_submatrices += curr
        
        return number_submatrices
