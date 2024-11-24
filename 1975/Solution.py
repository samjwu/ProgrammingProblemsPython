class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        ans = 0
        low = float("inf")
        negativeCount = 0

        for i in range(m):
            for j in range(n):
                val = matrix[i][j]

                ans += abs(val)
                
                if val < 0:
                    negativeCount += 1

                low = min(low, abs(val))

        # even negatives cancel out
        # if there is an odd negative, remove twice the lowest value
        # from the max possible answer
        if negativeCount % 2 != 0:
            ans -= 2 * low

        return ans
