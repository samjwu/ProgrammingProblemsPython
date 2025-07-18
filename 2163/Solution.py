import heapq
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
        To minimize difference of left and right parts,
        minimize the left and maximize the right
        """
        n = len(nums) // 3

        # store the minimum possible sum of the left
        left_part = [0] * (n + 1)

        # base case: sum of first n elements
        left_sum = sum(nums[:n])
        left_part[0] = left_sum

        # use max heap to keep smallest n elements
        max_heap = [-x for x in nums[:n]]
        heapq.heapify(max_heap)

        # left part can include up to the (2n-1)th element
        for i in range(n, n*2):
            left_sum += nums[i]
            heapq.heappush(max_heap, -nums[i])
            left_sum -= -heapq.heappop(max_heap)
            left_part[i-(n-1)] = left_sum

        # store the maximum possible sum of the right
        right_part = sum(nums[n*2:])

        # use max heap to keep biggest n elements
        min_heap = nums[n*2:]
        heapq.heapify(min_heap)
        
        # base answer: diff of first third and last third
        min_diff = left_part[n] - right_part

        # right part can include down to the nth element
        for i in range(n*2-1, n-1, -1):
            right_part += nums[i]
            heapq.heappush(min_heap, nums[i])
            right_part -= heapq.heappop(min_heap)
            min_diff = min(min_diff, left_part[i-n] - right_part)

        return min_diff
