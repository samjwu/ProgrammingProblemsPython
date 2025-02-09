class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        diff_count = {}

        for i in range(n):
            # j - i = nums[j] - nums[i
            # j − nums[j] = i − nums[i]
            diff = i - nums[i]

            # good pairs = count of all prev positions with same diff
            good_pairs_count = diff_count.get(diff, 0)

            # bad pairs = all pairs - good pairs
            ans += i - good_pairs_count

            # increment count for current diff
            diff_count[diff] = good_pairs_count + 1

        return ans
