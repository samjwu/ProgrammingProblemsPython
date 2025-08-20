from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        # memo[i][j] = size of largest square with all ones
        # whose bottom right corner is (i-1, j-1) in matrix
        memo = [[0 for j in range(n+1)] for i in range(m+1)]
        squares = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    # largest square at current position
                    # is an extension of the smallest sqaure among 3 locations:
                    # top left, top, and the left
                    # plus one since the current position is one
                    memo[i+1][j+1] = min(memo[i][j], memo[i+1][j], memo[i][j+1]) + 1
                    # square of size x has x subsquares with the same bottom right corner
                    squares += memo[i+1][j+1]

        return squares
