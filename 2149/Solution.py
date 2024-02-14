class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [0] * n
        
        plus = 0
        minus = 1

        for i in range(n):
            if nums[i] > 0:
                ans[plus] = nums[i]
                plus += 2
            else:
                ans[minus] = nums[i]
                minus += 2

        return ans
