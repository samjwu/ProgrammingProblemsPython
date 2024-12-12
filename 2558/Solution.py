class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = []
        
        for gift in gifts:
            heapq.heappush(maxHeap, -gift)
            
        for i in range(k):
            gift = -heapq.heappop(maxHeap)
            leave = floor(gift**0.5)
            heapq.heappush(maxHeap, -leave)
            
        ans = 0
        
        while maxHeap:
            gift = -heapq.heappop(maxHeap)
            ans += gift
            
        return ans
