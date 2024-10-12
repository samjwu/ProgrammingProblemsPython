class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # mark starts as positive, end as negative
        # extend end by 1 for inclusive interval
        points = []
        for interval in intervals:
            points.append((interval[0], 1))
            points.append((interval[1] + 1, -1))

        points.sort(key=lambda x: (x[0], x[1]))

        overlaps = 0

        # max number of overlaps is equivalent
        # to min num of groups needed
        ans = 0

        for point in points:
            overlaps += point[1]
            ans = max(ans, overlaps)

        return ans
