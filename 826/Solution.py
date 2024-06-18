class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        m = len(worker)
        
        # add a 0 difficulty job for workers who cannot do anything
        jobs = [(0, 0)]
        
        for i in range(n):
            jobs.append((difficulty[i], profit[i]))
            
        jobs.sort()
        
        # if easier job has more profit, take that job instead
        for i in range(n):
            jobs[i+1] = (
                jobs[i+1][0],
                max(jobs[i][1], jobs[i + 1][1]),
            )
            
        ans = 0
        
        for i in range(m):
            # binary search to get hardest job worker can do
            l = 0
            r = n
            gain = 0

            while l <= r:
                mid = (l + r) // 2

                if jobs[mid][0] <= worker[i]:
                    gain = max(gain, jobs[mid][1])
                    l = mid+1
                else:
                    r = mid-1
            
            ans += gain
            
        return ans
