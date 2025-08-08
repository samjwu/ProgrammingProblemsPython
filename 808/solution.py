from collections import defaultdict


class Solution:
    # memo[i][j] = probability of using up soup A first
    # where i is number of servings left of soup A
    # and j is number of servings left of soup B
    memo = defaultdict(dict)

    def soupServings(self, n: int) -> float:
        # use magic number
        # if n = 5550, probability = 0.9999989925525751
        if n >= 5550:
            return 1

        def recurse(i: int, j: int) -> float:
            # use precomputed value if available
            if i in self.memo and j in self.memo[i]:
                return self.memo[i][j]

            # both are empty
            # so 50/50 chance of using up soup A first
            if i <= 0 and j <= 0:
                return 0.5

            # used up soup A first
            # 100% chance of using up soup A first
            if i <= 0:
                return 1.0

            # used up soup B first
            # 0% chance of using up soup A first
            if j <= 0:
                return 0.0

            # try all possible pours
            # combine their probabilities then divide by 4
            # to account for 4 possible outcomes
            self.memo[i][j] = (
                recurse(i-4, j)
                + recurse(i-3, j-1)
                + recurse(i-2, j-2)
                + recurse(i-1, j-3)
            ) / 4.0
            return self.memo[i][j]
        
        # treat each 25ml as a serving
        # take ceil for any remainder
        # since 5ml left is still a serving
        servings = ceil(n / 25)

        return recurse(servings, servings)
