import heapq
from collections import Counter
from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        max_heap = []

        for n in nums:
            heapq.heappush(max_heap, n)
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        freq = Counter(max_heap)
        max_subseq = []

        for n in nums:
            if freq[n] > 0:
                freq[n] -= 1
                max_subseq.append(n)

        return max_subseq
