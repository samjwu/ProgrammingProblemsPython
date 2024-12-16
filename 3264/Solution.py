class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minHeap = []
        
        n = len(nums)
        
        for i in range(n):
            heapq.heappush(minHeap, (nums[i], i))
            
        for i in range(k):
            low, idx = heapq.heappop(minHeap)
            heapq.heappush(minHeap, (low * multiplier, idx))
            
        ans = [-1 for i in range(n)]
        
        for i in range(n):
            val, idx = heapq.heappop(minHeap)
            ans[idx] = val
            
        return ans
