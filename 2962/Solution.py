class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        ans = 0
        hi = max(nums)
        hi_count = 0
        left = 0

        for right in range(n):
            if nums[right] == hi:
                hi_count += 1

            while hi_count == k:
                if nums[left] == hi:
                    hi_count -= 1
                left += 1

            # for window ending at right
            # there are left + 1 starting positions (from 0)
            ans += left

        return ans
