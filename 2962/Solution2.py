class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        hi = max(nums)
        hi_indices = []

        for idx, num in enumerate(nums):
            if num == hi:
                hi_indices.append(idx)

            hi_count = len(hi_indices)
            # count number of subarrays ending at idx
            # where hi appears at least k times
            if hi_count >= k:
                # hi_indices[-k] is equivalent to left
                # from the sliding window solution
                # add 1 since it's 0-indexed
                ans += hi_indices[-k] + 1

        return ans
