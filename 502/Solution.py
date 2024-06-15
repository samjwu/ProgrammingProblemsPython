class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(capital)
        
        projects = sorted(zip(capital, profits), key=lambda project: project[0])
        
        maxHeap = []
        
        idx = 0
        
        for i in range(k):
            while idx < n and projects[idx][0] <= w:
                heapq.heappush(maxHeap, -projects[idx][1])
                idx += 1
                
            if maxHeap:
                w += -1 * heapq.heappop(maxHeap)
            
        return w
