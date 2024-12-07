class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)

        while l < r:
            m = (l + r) // 2

            if self.canDivide(m, nums, maxOperations):
                r = m
            else:
                l = m + 1

        return l

    def canDivide(self, maxBagSize, nums, maxOperations) -> bool:
        """
        Return true if balls can be divided in maxOperations moves
        such that max number of balls is maxBagSize.
        """
        ops = 0

        for num in nums:
            operations = math.ceil(num / maxBagSize) - 1
            ops += operations

            if ops > maxOperations:
                return False

        return True
