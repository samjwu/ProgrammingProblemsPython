class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min_heap = []

        n = len(nums)

        for i in range(1, n):
            heappush(min_heap, -nums[i])

            if len(min_heap) > 2:
                heappop(min_heap)

        return nums[0] - min_heap[0] - min_heap[1]
