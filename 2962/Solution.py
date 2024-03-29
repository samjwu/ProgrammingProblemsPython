class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        hi = max(nums)

        n = len(nums)

        ans = 0
        
        left = 0
        
        hiCount = 0

        for right in range(n):
            if nums[right] == hi:
                hiCount += 1

            while hiCount == k:
                if nums[left] == hi:
                    hiCount -= 1
                left += 1

            # for window ending at right
            # there are left + 1 starting positions (from 0)
            ans += left
        return ans
