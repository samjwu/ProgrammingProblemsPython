class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # memo[x] = probability of hitting x points
        memo = [0 for i in range(n+1)]
        # probability of hitting 0 points is 100% at start
        memo[0] = 1

        # track probability of scores in a window
        # while score is still less than k
        window = 1 if k > 0 else 0

        # try all scores from 1 to n
        for i in range(1, n+1):
            # probability of hitting i points is equal to
            # probability sum of all previous scores
            # divided by number of possible points
            memo[i] = window / maxPts

            # new score can still be added to if less than k
            # so add probability of hitting i to the window
            if i < k:
                window += memo[i]

            # new score exceeds the max points possible in 1 draw
            # therefore remove all previous probabilities outside of the window
            # which is the new score - max points in 1 draw (i - maxPts)
            if i >= maxPts and i - maxPts < k:
                window -= memo[i - maxPts]

        # return probability range of k to n points
        return sum(memo[k:])
