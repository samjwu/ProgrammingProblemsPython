class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        max_len = 0
        # memo[prev][curr] = max len subseq based on remainders where
        # last element % k = curr
        # and second last element % k = prev
        memo = [[0] * k for i in range(k)]

        for curr in nums:
            curr %= k

            for prev in range(k):
                # get new max len subseq by extending a previously existing one
                # memo[curr][prev] = max len subseq ending with remainder prev
                # memo[prev][curr] = max len subseq ending with remainder curr
                # therefore we want remainders in the order:
                # 3rd last, 2nd last, and last > curr, prev, curr
                memo[prev][curr] = memo[curr][prev] + 1
                max_len = max(max_len, memo[prev][curr])

        return max_len
