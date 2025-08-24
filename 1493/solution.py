from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        # can delete up to one 0
        can_delete = 1

        # define start and end of sliding window
        # window has longest subarray of 1s
        # with up to one deleted 0
        start = 0
        for end in range(len(nums)):
            # delete a 0 if it is encountered
            if nums[end] == 0:
                can_delete -= 1

            # if used too many deletions
            # then keep shrinking the window
            if can_delete < 0:
                can_delete += nums[start] == 0
                start += 1

            # the window size is end - start + 1
            # but since window contains a 0, subtract one
            # therefore candidate answer is end - start + 1 - 1
            # = end - start
            longest = max(longest, end - start)

        return longest
