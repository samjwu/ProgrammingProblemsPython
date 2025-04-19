class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]

        for i in range(1, n):
            if nums[i-1] + 1 == nums[i]:
                ans += nums[i]
            else:
                break

        nums.sort()

        for i in range(n):
            if ans == nums[i]:
                ans += 1

        return ans
