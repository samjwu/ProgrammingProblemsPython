class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        m = len(queries)
        n = len(nums)

        left = 0
        right = m

        if not self.can_zero(nums, queries, right):
            return -1

        while left <= right:
            middle = left + (right - left) // 2

            if self.can_zero(nums, queries, middle):
                right = middle - 1
            else:
                left = middle + 1

        return left

    def can_zero(self, nums: List[int], queries: List[List[int]], k: int) -> bool:
        n = len(nums)
        running = 0
        # to keep track of queries
        difference_array = [0] * (n + 1)

        for i in range(k):
            # update start and end of query by val
            start, end, val = queries[i]

            # increment start to signify val subtraction
            # since the query allows subtracting val from start to end
            difference_array[start] += val
            # decrement end + 1 to signify end of val subtraction
            # since the query stops
            difference_array[end + 1] -= val

        for i in range(n):
            running += difference_array[i]

            # running below number means cannot subtract to 0
            if running < nums[i]:
                return False

        return True
