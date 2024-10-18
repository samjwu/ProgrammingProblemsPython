class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            ans |= num

        return self.countSubsets(nums, 0, 0, ans)

    def countSubsets(self, nums: List[int], idx: int, curr: int, target: int) -> int:
        if idx == len(nums):
            if curr == target:
                return 1
            else:
                return 0

        skip = self.countSubsets(nums, idx + 1, curr, target)

        include = self.countSubsets(nums, idx + 1, curr | nums[idx], target)

        return skip + include
