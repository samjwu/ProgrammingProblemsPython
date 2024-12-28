class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # track index of best answer for 1, 2, and 3 windows
        ans1 = 0
        ans2 = [0, k]
        ans3 = [0, k, k*2]

        # track sum of each window
        windowSum1 = sum(nums[0:k])
        windowSum2 = sum(nums[k:k*2])
        windowSum3 = sum(nums[k*2:k*3])

        # track highest sum of 1, 2, and 3 windows
        bestSum1 = windowSum1
        bestSum2 = windowSum1 + windowSum2
        bestSum3 = windowSum1 + windowSum2 + windowSum3

        # track current position of each window
        idx1 = 1
        idx2 = k + 1
        idx3 = k*2 + 1

        while idx3 <= n - k:
            # slide each window
            windowSum1 += nums[idx1 + k - 1] - nums[idx1 - 1]
            windowSum2 += nums[idx2 + k - 1] - nums[idx2 - 1]
            windowSum3 += nums[idx3 + k - 1] - nums[idx3 - 1]
            
            # update trackers for 1 window
            if windowSum1 > bestSum1:
                ans1 = idx1
                bestSum1 = windowSum1

            # update trackers for 2 windows
            if windowSum2 + bestSum1 > bestSum2:
                ans2 = [ans1, idx2]
                bestSum2 = windowSum2 + bestSum1

            # update trackers for 3 windows
            if windowSum3 + bestSum2 > bestSum3:
                ans3 = ans2 + [idx3]
                bestSum3 = windowSum3 + bestSum2

            # slide each window
            idx1 += 1
            idx2 += 1
            idx3 += 1

        return ans3
