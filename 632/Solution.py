class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)

        # val, index of list, index of val in list
        minHeap = []
        
        hi = float("-inf")

        start = float("-inf")
        end = float("inf")

        # include first/smallest val in each list in heap
        for i in range(n):
            heapq.heappush(minHeap, (nums[i][0], i, 0))
            hi = max(hi, nums[i][0])

        while len(minHeap) == n:
            # remove smallest element from heap
            lo, i, j = heapq.heappop(minHeap)

            # check for candidate answer
            if hi - lo < end - start:
                start = lo
                end = hi

            # add next val from same list to heap
            if j + 1 < len(nums[i]):
                heapq.heappush(minHeap, (nums[i][j+1], i, j+1))
                hi = max(hi, nums[i][j+1])

        return [start, end]
