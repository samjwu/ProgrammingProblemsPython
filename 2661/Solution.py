class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        # painted_row[i] = number of squares painted in row i
        painted_row = [0 for i in range(m)]
        # painted_col[i] = number of squares painted in col i
        painted_col = [0 for i in range(n)]

        num_idx = {}

        for row in range(m):
            for col in range(n):
                num_idx[mat[row][col]] = [row, col]

        for i in range(m*n):
            num = arr[i]
            row, col = num_idx[num]

            painted_row[row] += 1
            painted_col[col] += 1

            if painted_row[row] == n or painted_col[col] == m:
                return i

        return -1
