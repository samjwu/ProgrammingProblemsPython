class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        # iterate from end of window
        for i in range(2, n):
            # check start of window
            if nums[i - 2] == 0:
                ans += 1
                # flip all 3 in window
                nums[i - 2] = nums[i - 2] ^ 1
                nums[i - 1] = nums[i - 1] ^ 1
                nums[i] = nums[i] ^ 1

        if sum(nums) == n:
            return ans

        return -1
