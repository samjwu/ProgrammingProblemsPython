class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        bit_mask = 0
        left = 0

        for right in range(n):
            # shrink window while invalid
            while bit_mask & nums[right] != 0:
                bit_mask ^= nums[left]
                left += 1

            # expand window
            bit_mask |= nums[right]

            ans = max(ans, right - left + 1)

        return ans
