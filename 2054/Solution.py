class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        starts = events[:]
        ends = events[:]
        
        starts.sort(key=lambda x: x[0])
        ends.sort(key=lambda x: x[1])
        
        i = 0
        j = 0
        
        n = len(events)
        
        bestPastVal = 0
        ans = 0
        
        while i < n:
            while j < n and ends[j][1] < starts[i][0]:
                bestPastVal = max(bestPastVal, ends[j][2])
                j += 1
                
            ans = max(ans, starts[i][2] + bestPastVal)
            i += 1
            
        return ans
