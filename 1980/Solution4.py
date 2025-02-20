class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        ans = []

        # form answer by selecting the opposite digit
        # at the ith index for the ith number
        # therefore the final answer will differ from every number in nums
        # in at least one position
        for i in range(n):
            digit = nums[i][i]
            
            if digit == "0":
                ans.append("1")
            else:
                ans.append("0")
        
        return "".join(ans)
