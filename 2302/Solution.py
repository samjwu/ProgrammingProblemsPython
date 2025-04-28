class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        ans = 0
        total = 0
        i = 0
        
        for j in range(n):
            # add to window
            total += nums[j]

            # shrink window
            while i <= j and total * (j - i + 1) >= k:
                total -= nums[i]
                i += 1

            ans += j - i + 1

        return ans
