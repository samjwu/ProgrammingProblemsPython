class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        travelDays = set(days)
        memo = {}

        def recurse(today):
            if today > days[-1]:
                return 0

            if today not in travelDays:
                return recurse(today + 1)

            if today in memo:
                return memo[today]

            one = recurse(today + 1) + costs[0]
            seven = recurse(today + 7) + costs[1]
            thirty = recurse(today + 30) + costs[2]

            memo[today] = min(one, seven, thirty)
            return memo[today]

        return recurse(0)
