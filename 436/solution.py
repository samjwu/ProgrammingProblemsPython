import bisect
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # sort by start
        # include index of each interval for use in answer
        sorted_intervals = sorted([[start, end, idx] for idx, [start, end] in enumerate(intervals)])

        # extract starts for use in binary search
        starts = [start for start, end, idx in sorted_intervals]

        right_intervals = [-1] * n

        for start, end, idx in sorted_intervals:
            # find the first start greater than or equal to this end
            right = bisect.bisect_left(starts, end)
            if right < n:
                right_intervals[idx] = sorted_intervals[right][2]
        
        return right_intervals
