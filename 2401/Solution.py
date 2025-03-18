class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        right = n
        ans = 1

        while left <= right:
            mid = left + (right - left) // 2
            
            if self.is_nice(mid, nums, n):
                # found candidate, so try longer
                ans = mid
                left = mid + 1
            else:
                # no candidate, so shorten
                right = mid - 1

        return ans

    def is_nice(self, length: int, nums: list[int], n: int) -> bool:
        if length <= 1:
            return True

        # try current length, for all possible indices
        for i in range(n - length + 1):
            bit_mask = 0
            is_nice = True

            for j in range(i, i + length):
                if bit_mask & nums[j] != 0:
                    is_nice = False
                    break
                bit_mask |= nums[j]

            if is_nice:
                return True

        return False
