class Solution:
    def maximumCandies(self, candies, k):
        # find max candy that can be distributed per child
        hi = 0
        for candy in candies:
            hi = max(hi, candy)

        left = 0
        right = hi

        while left < right:
            middle = (left + right + 1) // 2

            if self.is_valid_allocation(candies, k, middle):
                # middle is possible option
                left = middle
            else:
                # middle is not possible option
                right = middle - 1

        return left

    def is_valid_allocation(self, candies, k, distribute):
        children_satisfied = 0

        for candy in candies:
            # allocate pile to max number of children
            children_satisfied += candy // distribute
                
        return children_satisfied >= k
