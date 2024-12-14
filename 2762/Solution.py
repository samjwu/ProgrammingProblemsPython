class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # store value and index
        minHeap = []
        maxHeap = []

        l = 0
        r = 0
        ans = 0

        while r < len(nums):
            # grow window
            heapq.heappush(minHeap, (nums[r], r))
            heapq.heappush(maxHeap, (-nums[r], r))

            # shrink window if violates condition
            while l < r and -maxHeap[0][0] - minHeap[0][0] > 2:
                l += 1

                # pop indices that are left of the window
                while minHeap and minHeap[0][1] < l:
                    heapq.heappop(minHeap)
                while maxHeap and maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)

            # add all valid subarrays ending at r
            # given by r - l + 1
            # [l, r], [l+1, r], ... [r, r]
            ans += r - l + 1
            
            r += 1

        return ans
