from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # construct prefix sum
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        def mergesort(low: int, high: int) -> int:
            # base case
            # subarray has length 1 or less, cannot form range sum
            if high - low <= 1:
                return 0

            # split into two halves
            mid = (low + high) // 2
            
            # recursively count range sums in halves
            # total count = left half + right half + overlap
            count = mergesort(low, mid) + mergesort(mid, high)

            # count the overlap
            i = mid
            j = mid
            # all prefix sums from left half is contained in prefix_sum[low:mid]
            # all prefix sums from right half is contained in prefix_sum[mid:high]
            # need to find all difference of right and left prefix sums
            # lower <= right_prefix_sum - left_prefix_sum <= upper
            for left_prefix_sum in prefix_sum[low:mid]:
                # find minimum i such that right_prefix_sum - left_prefix_sum >= lower
                while i < high and prefix_sum[i] - left_prefix_sum < lower:
                    i += 1
                # find max j such that right_prefix_sum - left_prefix_sum > upper
                while j < high and prefix_sum[j] - left_prefix_sum <= upper:
                    j += 1
                # overlap is the difference in pointers
                # since j is outside the bound but i is inside
                count += j - i

            # merge and sort the two halves
            prefix_sum[low:high] = sorted(prefix_sum[low:high])

            return count

        return mergesort(0, len(prefix_sum))
