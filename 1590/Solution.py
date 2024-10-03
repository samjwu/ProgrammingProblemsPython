class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)

        totalRemainder = 0

        for num in nums:
            totalRemainder = (totalRemainder + num) % p

        targetRemainder = totalRemainder % p

        if targetRemainder == 0:
            return 0

        prefixSumRemainder = {}
        # for impossible case
        prefixSumRemainder[0] = -1

        currentRemainder = 0

        ans = n

        for i in range(n):
            currentRemainder = (currentRemainder + nums[i]) % p

            # calc needed prefix sum remainder for comparison
            neededRemainder = (currentRemainder - targetRemainder + p) % p

            # if it was seen before, found a possible answer
            if neededRemainder in prefixSumRemainder:
                ans = min(ans, i - prefixSumRemainder[neededRemainder])

            # keep track of current remainder as needed remainder for future iterations
            prefixSumRemainder[currentRemainder] = i

        if ans == n:
            return -1
        return ans
