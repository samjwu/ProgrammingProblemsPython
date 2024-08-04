class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 1e9 + 7

        n = len(nums)

        subarraySums = []
        
        for i in range(n):
            subSum = 0

            for j in range(i, n):
                subSum += nums[j]
                subarraySums.append(subSum)

        subarraySums.sort()

        ans = 0

        for i in range(left - 1, right):
            ans = (ans + subarraySums[i]) % MOD

        return int(ans)
