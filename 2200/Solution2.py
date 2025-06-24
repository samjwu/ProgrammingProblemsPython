from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        n = len(nums)

        key_indices = [j for j in range(n) if nums[j] == key]

        for i in range(n):
            if any(abs(i - j) <= k for j in key_indices):
                ans.append(i)

        return ans
