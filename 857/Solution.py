class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)

        ans = float("inf")
        
        qualitySum = 0
        
        # expectation = wage / quality
        expectation = []

        for i in range(n):
            expectation.append((wage[i] / quality[i], quality[i]))

        expectation.sort(key=lambda x: x[0])

        maxHeap = []

        for i in range(n):
            heapq.heappush(maxHeap, -expectation[i][1])
            
            qualitySum += expectation[i][1]

            if len(maxHeap) > k:
                qualitySum += heapq.heappop(maxHeap)

            if len(maxHeap) == k:
                ans = min(ans, qualitySum * expectation[i][0])

        return ans
