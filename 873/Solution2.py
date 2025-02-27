class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        n = len(arr)
        ans = 0

        # memo[i][j] = longest ans ending at indices i and j
        memo = [[0] * n for _ in range(n)]

        val_to_idx = {num: idx for idx, num in enumerate(arr)}

        for third in range(n):
            for second in range(third):
                diff = arr[third] - arr[second]
                first = val_to_idx.get(diff, -1)

                # first must exist for valid answer
                # diff must be smaller than second for subanswer to increase
                if first >= 0 and diff < arr[second]:
                    memo[second][third] = memo[first][second] + 1
                else:
                    memo[second][third] = 2

                ans = max(ans, memo[second][third])

        if ans <= 2:
            return 0
        return ans
