class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1e9 + 7

        n = len(corridor)

        # max 2 seats per division
        memo = [[-1] * 3 for i in range(n)]
        
        def recurse(index: int, seats: int) -> int:
            if index == n:
                if seats == 2:
                    return 1
                return 0
            
            if memo[index][seats] != -1:
                return memo[index][seats]

            # have 2 seats, which is enough for a division
            if seats == 2:
                # only 2 seats allowed, must divide
                if corridor[index] == "S":
                    result = recurse(index + 1, 1)
                # can divide or continue
                else:
                    divide = recurse(index + 1, 0)
                    no_divide = recurse(index + 1, 2)
                    result = (divide + no_divide) % MOD
            # must continue until 2 seats
            else:
                if corridor[index] == "S":
                    result = recurse(index + 1, seats + 1)
                else:
                    result = recurse(index + 1, seats)
            
            memo[index][seats] = int(result)
            return memo[index][seats]
        
        return recurse(0, 0)
