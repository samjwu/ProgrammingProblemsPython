from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        
        diagonals = defaultdict(list)

        # add all elements from row 0 to row m-1
        # in reverse diagonal order (/)
        # from left to right starting at column 0
        for i in range(m):
            x = i
            y = 0

            while x > -1 and y < n:
                diagonals[i].append(mat[x][y])
                x -= 1
                y += 1

        # add all elements from column 1 to column
        # in reverse diagonal order (/)
        # from bottom to top starting at row m-1
        for j in range(1, n):
            x = m-1
            y = j

            while x > -1 and y < n:
                diagonals[m-1 + j].append(mat[x][y])
                x -= 1
                y += 1

        diagonal_order = []

        # add saved diagonals to the answer
        for k in range(m+n-1):
            to_add = diagonals[k]
            # for every odd diagonal, reverse traversal
            # since order is right to left on odd
            # and left to right on even
            if k % 2 == 1:
                to_add.reverse()
            diagonal_order += to_add

        return diagonal_order
