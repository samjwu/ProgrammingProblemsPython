class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        left = 0
        right = n - 1
        
        # get index of smallest number and set to left
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        
        def binarySearch(left_boundary, right_boundary, target):
            left = left_boundary
            right = right_boundary
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            return -1
        
        
        # check left
        ans = binarySearch(0, left - 1, target)
        if ans != -1:
            return ans
        
        # check right
        return binarySearch(left, n - 1, target)
