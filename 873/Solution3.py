class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        n = len(arr)
        ans = 0

        # memo[i][j] = longest ans ending at indices i and j
        memo = [[0] * n for _ in range(n)]

        # try all pairs summing to arr[idx]
        for idx in range(2, n):
            # two pointers
            left = 0
            right = idx - 1

            while left < right:
                pair_sum = arr[left] + arr[right]

                if pair_sum > arr[idx]:
                    right -= 1
                elif pair_sum < arr[idx]:
                    left += 1
                else:
                    memo[right][idx] = memo[left][right] + 1
                    ans = max(memo[right][idx], ans)
                    right -= 1
                    left += 1

        if ans > 0:
            return ans + 2
        return 0
