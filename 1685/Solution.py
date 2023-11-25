class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)

        running_sum = 0
        prefix_sum = []

        for i in range(n):
            running_sum += nums[i]
            prefix_sum.append(running_sum)
        
        ans = []

        for i in range(n):
            left_sum = prefix_sum[i] - nums[i]
            right_sum = prefix_sum[n-1] - prefix_sum[i]
            
            left_diff = nums[i] * i - left_sum
            right_diff = right_sum - nums[i] * (n-1 - i)

            ans.append(left_diff + right_diff)
        
        return ans
