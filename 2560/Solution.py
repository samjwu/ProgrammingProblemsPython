class Solution:
    def minCapability(self, nums, k):
        n = len(nums)

        # binary search on capability
        lo = 1
        hi = max(nums)

        while lo < hi:
            # steal from at most mid value
            mid = lo + (hi - lo) // 2
            steal = 0

            index = 0
            while index < n:
                if nums[index] <= mid:
                    # steal from current and skip next
                    steal += 1
                    index += 2
                else:
                    # skip current
                    index += 1

            if steal >= k:
                # stole from enough houses
                # mid is a candidate answer
                hi = mid
            else:
                # did not steal from enough houses
                # mid is not a candidate answer
                lo = mid + 1

        return lo
