class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        ans = 0

        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))

            ans += 1

        return ans
