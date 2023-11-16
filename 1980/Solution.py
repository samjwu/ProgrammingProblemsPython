class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        
        if n == 1:
            if nums[0] == "0":
                return "1"
            else:
                return "0"
        
        hi = 2**n - 1
        
        for i in range(hi):
            binary = self.toBinary(i, n)
            
            if binary not in nums:
                return binary
            
        return ""
            
    def toBinary(self, num: int, l: int) -> str:
        ans = ""
        
        for i in range(l):
            if num % 2 == 1:
                ans += "1"
            else:
                ans += "0"
            num >>= 1
            
        return ans[::-1]
