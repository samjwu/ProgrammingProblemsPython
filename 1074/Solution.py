class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        # prefix sum
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]
                
        # ansMap[x] = num of submatrices with sum x
        ansMap = defaultdict(int)
        ans = 0
        
        # start col num
        for j in range(n):
            # end col num
            for k in range(j, n):
                submatrixSum = 0
                ansMap.clear()
                ansMap[0] = 1
                
                # row num
                for i in range(m):
                    submatrixSum += matrix[i][k]
                    
                    # adjust prefix sum value to exclude elements left of submatrix
                    if j > 0:
                        submatrixSum -= matrix[i][j-1]
                        
                    # try removing all possible previously computed submatrices
                    # above the current submatrix
                    ans += ansMap[submatrixSum - target]
                    
                    # add current submatrix to map
                    ansMap[submatrixSum] += 1
        
        return ans
