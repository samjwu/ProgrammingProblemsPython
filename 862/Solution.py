class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        ans = float("inf")

        totalSum = 0
        
        prefixSumMinHeap = []

        for i, num in enumerate(nums):
            totalSum += num

            if totalSum >= k:
                ans = min(ans, i+1)

            # try removing subarrs if the resulting sum is at least k
            while prefixSumMinHeap and totalSum - prefixSumMinHeap[0][0] >= k:
                ans = min(ans, i - heappop(prefixSumMinHeap)[1])

            # add current total and index to heap
            heappush(prefixSumMinHeap, (totalSum, i))

        if ans == float("inf"):
            return -1
        return ans
