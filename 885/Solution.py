class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        n = rows * cols

        ans = []

        currRow = rStart
        currCol = cStart

        currDir = 0

        # to track number of steps to take in current direction
        walkSteps = 1

        while len(ans) < n:
            # each spiral has 2 sides with same length
            for i in range(2):
                for j in range(walkSteps):
                    if (currRow >= 0 and currRow < rows and currCol >= 0 and currCol < cols):
                        ans.append([currRow, currCol])

                    currRow += dir[currDir][0]
                    currCol += dir[currDir][1]

                currDir = (currDir + 1) % 4

            walkSteps += 1

        return ans
