class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            digits = int(math.floor(math.log10(num))) + 1
            
            if digits % 2 == 0:
                ans += 1

        return ans
