class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # bubble sort
        for i in range(n):
            for j in range(n-1-i):
                if nums[j] > nums[j+1]:
                    # check if set bits are equal to allow swap
                    if bin(nums[j]).count("1") == bin(nums[j + 1]).count("1"):
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                    else:
                        return False

        return True
