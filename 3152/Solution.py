class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        m = len(queries)

        ans = [False] * m

        # key: input index
        # value: number of continuous special subarrays (from 0)
        diffParity = [0] * n
        diffParity[0] = 0

        for i in range(1, n):
            diffParity[i] = diffParity[i-1]

            if nums[i-1] % 2 == nums[i] % 2:
                diffParity[i] += 1

        for i in range(m):
            start = queries[i][0]
            end = queries[i][1]

            # true if in same special subarray
            ans[i] = diffParity[end] - diffParity[start] == 0

        return ans
