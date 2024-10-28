class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        ans = 0
        
        seen = set(nums)

        for num in nums:
            square = num
            streak = 0

            while square in seen:
                streak += 1

                if square * square > 10**5:
                    break

                square *= square

            ans = max(ans, streak)

        if ans >= 2:
            return ans
        return -1
