class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        
        dividers = [arr[n // 4], arr[n // 2], arr[3 * n // 4]]
        
        for num in dividers:
            left = bisect_left(arr, num)
            right = bisect_right(arr, num) - 1
            
            if right - left + 1 > n/4:
                return num
            
        return -1
