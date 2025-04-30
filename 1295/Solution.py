class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            s = str(num)

            if len(s) % 2 == 0:
                ans += 1

        return ans
