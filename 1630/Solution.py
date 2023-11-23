class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        ans = []
        
        for i in range(m):
            arr = nums[l[i]:r[i]+1]
            ans.append(self.is_arithmetic(arr))
        
        return ans
    
    def is_arithmetic(self, arr: List[int]) -> bool:
        arr.sort()
        
        diff = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False

        return True
