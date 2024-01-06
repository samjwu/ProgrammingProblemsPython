class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profits: List[int]) -> int:
        # sort by end time
        jobs = sorted(zip(startTime, endTime, profits), key=lambda job: job[1])
        
        # memoize end time and profit pairs
        memo = [[0, 0]]
        
        for start, end, profit in jobs:
            # get index of element in memo with
            # highest profit up to start time of current job
            prevIdx = bisect_left(memo, [start + 1]) - 1
            
            # if the sum of
            # highest profit up to start time of current job
            # and profit of current job exceeds
            # highest profit up to latest end time
            # then add new element to memo
            if memo[prevIdx][1] + profit > memo[-1][1]:
                memo.append([end, memo[prevIdx][1] + profit])
                
        # loop invariant: latest end time in memo has highest profit
        # due to sort by end time
        return memo[-1][1]
