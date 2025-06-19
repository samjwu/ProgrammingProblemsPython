class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()

        num_subseq = 1
        low = nums[0]

        for num in nums:
            if num - low > k:
                num_subseq += 1
                low = num
                
        return num_subseq
