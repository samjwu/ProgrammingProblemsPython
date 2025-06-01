class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ways_to_distribute = 0

        # try all possible distributions for 1st child
        for first in range(min(limit, n) + 1):
            # invalid distribution
            remaining = n - first
            if remaining > limit * 2:
                continue

            # 2nd child can get at most min(remaining, limit)
            upper = min(remaining, limit)
            # 2nd child can get at least max(0, remaining - limit)
            lower = max(0, remaining - limit)

            # the range is the number of distributions for 2nd/3rd child
            # given fixed distribution for 1st child each iteration
            ways_to_distribute += upper - lower + 1

        return ways_to_distribute
