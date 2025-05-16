class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        cols = [-1] * n

        for i in range(m):
            for j in range(n):
                cols[j] = max(cols[j], matrix[i][j])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = cols[j]

        return matrix
