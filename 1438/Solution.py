class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0
        
        n = len(nums)
        
        # holds pairs (value, index)
        maxHeap = []
        minHeap = []

        left = 0
        
        for right in range(n):
            heapq.heappush(maxHeap, (-nums[right], right))
            heapq.heappush(minHeap, (nums[right], right))
            
            while -maxHeap[0][0] - minHeap[0][0] > limit:
                left = min(maxHeap[0][1], minHeap[0][1]) + 1
                
                while maxHeap[0][1] < left:
                    heapq.heappop(maxHeap)
                    
                while minHeap[0][1] < left:
                    heapq.heappop(minHeap)
                    
            ans = max(ans, right - left + 1)

        return ans
