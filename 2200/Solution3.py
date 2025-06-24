from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        n = len(nums)
        # smallest index ont in answer yet
        right = 0

        for j in range(n):
            if nums[j] == key:
                # left must be at least equal to:
                # right to avoid duplicate answer
                # and j-k to stay within bounds
                left = max(right, j-k)
                # right must be at most:
                # end of the array
                # or end of the bounds
                right = min(n-1, j+k) + 1
                for i in range(left, right):
                    ans.append(i)

        return ans
