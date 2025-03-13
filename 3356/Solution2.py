class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        running = 0
        k = 0
        difference_array = [0] * (n + 1)

        for i in range(n):
            # use queries while current number cannot be subtracted to 0
            while running + difference_array[i] < nums[i]:
                k += 1

                # used all queries, cannot make 0
                if k > len(queries):
                    return -1

                left, right, val = queries[k - 1]

                # query only matters if it applies to current (or future) numbers
                # since past is already processed
                if right >= i:
                    # again skip past so take max of left or current index
                    difference_array[max(left, i)] += val
                    difference_array[right + 1] -= val

            running += difference_array[i]

        return k
