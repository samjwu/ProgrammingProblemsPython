class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        i = 0
        j = 0
        k = n-1
        
        while i <= k:
            if nums[i] == 0:
                # swap(nums[i], nums[j])
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                
                i += 1
                j += 1
            elif nums[i] == 1:
                i += 1
            else:
                # swap(nums[i], nums[k])
                tmp = nums[i]
                nums[i] = nums[k]
                nums[k] = tmp
                
                k -= 1
