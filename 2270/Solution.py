class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = []
        cur = 0

        for num in nums:
            cur += num
            prefix_sum.append(cur)

        ans = 0
        n = len(nums)

        for i in range(n - 1):
            left = prefix_sum[i]
            right = prefix_sum[n - 1] - left
            if left >= right:
                ans += 1

        return ans
