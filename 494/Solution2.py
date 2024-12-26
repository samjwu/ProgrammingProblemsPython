class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {(0, 0): 1}

        for i in range(n):
            copy = dict(memo)
            for (idx, val) in copy:
                if idx == i:
                    memo[(i+1, val + nums[i])] = memo.get((i+1, val + nums[i]), 0) + copy[(i, val)]
                    memo[(i+1, val - nums[i])] = memo.get((i+1, val - nums[i]), 0) + copy[(i, val)]

        return memo.get((n, target), 0)
        