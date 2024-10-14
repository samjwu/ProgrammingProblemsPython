class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        
        heapq.heapify(maxHeap)
            
        ans = 0
            
        for i in range(k):
            val = -heapq.heappop(maxHeap)
            ans += val
            heapq.heappush(maxHeap, -ceil(float(val)/3))
            
        return ans
