class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums)-1)
        return nums
        
    def quicksort(self, nums: List[int], start: int, end: int) -> None:
        if start < end:
            pivotIndex = self.partition(nums, start, end)
            self.quicksort(nums, start, pivotIndex-1)
            self.quicksort(nums, pivotIndex+1, end)
        
    def partition(self, nums: List[int], start: int, end: int) -> int: 
        pivot = nums[end]
        i = start-1
        
        for j in range(start, end):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                
        nums[i+1], nums[end] = nums[end], nums[i+1]
        
        return i+1
