class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp = [0] * len(nums)
        
        def mergeSort(left: int, right: int) -> None:
            # base case: if left/right are equal, there is only 1 element
            if left >= right:
                return
            
            mid = (left + right) // 2
            
            mergeSort(left, mid)
            mergeSort(mid + 1, right)
            
            merge(left, mid, right)
    
        def merge(left: int, mid: int, right: int) -> None:
            # left part: from left to mid
            start1 = left
            n1 = mid - left + 1
            
            # right part: from mid+1 to right
            start2 = mid + 1
            n2 = right - mid

            # copy both halves to a temporary array
            for i in range(n1):
                temp[start1 + i] = nums[start1 + i]
            for i in range(n2):
                temp[start2 + i] = nums[start2 + i]

            # merge temp array back into original array
            i, j, k = 0, 0, left
            while i < n1 and j < n2:
                if temp[start1 + i] <= temp[start2 + j]:
                    nums[k] = temp[start1 + i]
                    i += 1
                else:
                    nums[k] = temp[start2 + j]
                    j += 1
                k += 1

            while i < n1:
                nums[k] = temp[start1 + i]
                i += 1
                k += 1
            while j < n2:
                nums[k] = temp[start2 + j]
                j += 1
                k += 1
                
        mergeSort(0, len(nums) - 1)
        return nums
