class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # True for odd number of flips
        # False for even number (including 0) of flips
        flipParity = [False] * len(nums)

        # number of odd flips in previous flip
        goodPastFlips = 0

        ans = 0

        for i in range(n):
            if i >= k:
                # if previous flip was odd parity
                # then current flip reverses the effective flip back to 0
                if flipParity[i - k]:
                    goodPastFlips -= 1

            # if flip parity results in a 0 bit
            # then current window must be flipped
            if goodPastFlips % 2 == nums[i]:
                # window must be valid size
                # subarray must fit in array
                if i + k > len(nums):
                    return -1

                # perform flip on current bit
                goodPastFlips += 1
                flipParity[i] = True
                ans += 1

        return ans
