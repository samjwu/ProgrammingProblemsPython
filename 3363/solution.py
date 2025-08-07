from typing import List


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        # initialize to diagonal (first child path) (\)
        # since this is the minimum collected
        max_collected = sum(fruits[i][i] for i in range(n))

        def collect_max_fruit() -> int:
            """
            Follow path with most fruit

            Starting from the top right
            and ending at the bottom right
            """
            # prev[col] = max fruits collected to (prev row, col)
            prev = [float("-inf")] * n
            # curr[col] = max fruits collected to (curr row, col)
            curr = [float("-inf")] * n

            # must start at top right
            prev[n-1] = fruits[0][n-1]

            for i in range(1, n-1):
                # valid columns must be above the diagonal (\)
                for j in range(max(n-1-i, i+1), n):
                    # try moving down
                    best = prev[j]

                    # try moving down + left
                    if j-1 >= 0:
                        best = max(best, prev[j-1])
                    
                    # try moving down + right
                    if j+1 < n:
                        best = max(best, prev[j+1])

                    # take the best path
                    curr[j] = best + fruits[i][j]

                # special trick
                # technically only need to do:
                # prev = curr
                
                # however, for python, do a swap,
                # to avoid having both prev and curr
                # point to the same list object in memory
                prev, curr = curr, prev
                
            return prev[n-1]

        # simulate the second child path
        max_collected += collect_max_fruit()

        # flip the matrix along the diagonal (\)
        # so that we can reuse the helper function
        for i in range(n):
            for j in range(i):
                fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]

        # then reuse the helper function 
        # to simulate the third child path
        max_collected += collect_max_fruit()

        return max_collected
