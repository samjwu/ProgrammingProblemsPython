class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_sum = 0
        min_sum = 0
        # init to 0 to account for empty subarray
        max_sum = 0

        for num in nums:
            curr_sum += num

            # track max and min sum so far
            min_sum = min(min_sum, curr_sum)
            max_sum = max(max_sum, curr_sum)

        return max_sum - min_sum
