class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ans = float('inf')

        # assuming robot 1 takes bottom path
        # available score for robot 2 is top path
        top = sum(grid[0])
        bot = 0

        # move robot 1 to bottom path later for all columns
        # to simulate all possible path combos for both robots
        for i in range(n):
            top -= grid[0][i]
            # other path is zeroed, so robot 2 takes best remaining
            robot2_score = max(top, bot)
            ans = min(ans, robot2_score)
            bot += grid[1][i]

        return ans
