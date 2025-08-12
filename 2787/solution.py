from functools import cache


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def recurse(n: int, x: int, unique_int: int) -> int:
            remaining = n - unique_int ** x

            if remaining == 0:
                # found a way
                return 1
            elif remaining > 0:
                # don't include current unique int
                exclude_unique = recurse(n, x, unique_int + 1)
                # include current unique int
                include_unique = recurse(remaining, x, unique_int + 1)
                # total ways is all ways both including and excluding unique int
                return (exclude_unique + include_unique) % MOD
            else:
                # unique int ^ x is too high, no valid solution
                return 0

        return recurse(n, x, 1) % MOD
