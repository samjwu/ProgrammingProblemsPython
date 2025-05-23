class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0

        i = 0
        score = nums[i] + nums[i+1]
        ans = 0

        while n-2 >= i:
            if nums[i] + nums[i+1] == score:
                ans += 1
            else:
                break
                
            i += 2

        return ans
