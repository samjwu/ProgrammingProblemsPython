class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        n = len(arr)
        nums = set(arr)
        ans = 0

        # try all possible starting pairs
        for first in range(n):
            for second in range(first + 1, n):
                # O(1) space fibonacci check
                prev = arr[second]
                curr = arr[first] + arr[second]
                subans = 2

                while curr in nums:
                    # O(1) space fibonacci check
                    tmp = curr
                    curr += prev
                    prev = tmp

                    subans += 1
                    ans = max(ans, subans)

        return ans  
