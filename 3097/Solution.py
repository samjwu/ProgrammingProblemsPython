class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = float("inf")
        n = len(nums)

        bitFreq = [0] * 32

        start = 0
        end = 0
        
        while end < n:
            self.changeBitFreq(bitFreq, nums[end], 1)

            while (start <= end and self.bitToNum(bitFreq) >= k):
                ans = min(ans, end - start + 1)
                self.changeBitFreq(bitFreq, nums[start], -1)
                start += 1

            end += 1

        if ans == float("inf"):
            return -1
        return ans

    def changeBitFreq(self, bitFreq: list, num: int, change: int) -> None:
        for i in range(32):
            if num & (1 << i):
                bitFreq[i] += change

    def bitToNum(self, bitFreq: list) -> int:
        ans = 0

        for i in range(32):
            if bitFreq[i]:
                ans |= 1 << i

        return ans
