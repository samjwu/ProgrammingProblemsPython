class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = 0
        curr_sum = 0
        min_sum = float("inf")
        max_sum = float("-inf")

        for num in nums:
            curr_sum += num

            # track max and min sum so far
            min_sum = min(min_sum, curr_sum)
            max_sum = max(max_sum, curr_sum)

            # if current subarray has non-negative sum,
            # calc a possible answer by removing a prev subarray with minimum sum
            if curr_sum >= 0:
                ans = max([ans, curr_sum, curr_sum - min_sum])
            
            # if current subarray has non-positive sum,
            # calc a possible answer by removing a prev subarray with maximum sum
            if curr_sum <= 0:
                ans = max([ans, abs(curr_sum), abs(curr_sum - max_sum)])

        return ans
