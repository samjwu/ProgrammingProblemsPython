class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        n = len(dimensions)
        ans = -1
        longest_diagonal = -1

        for i in range(n):
            diagonal = dimensions[i][0]**2 + dimensions[i][1]**2

            if diagonal > longest_diagonal:
                ans = dimensions[i][0] * dimensions[i][1]
                longest_diagonal = diagonal
            elif diagonal == longest_diagonal:
                ans = max(ans, dimensions[i][0] * dimensions[i][1])
                
        return ans
