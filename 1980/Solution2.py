class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        
        if n == 1:
            if nums[0] == "0":
                return "1"
            else:
                return "0"
            
        seen = set()
        
        for num in nums:
            seen.add(int(num, 2))

        hi = 2**n - 1

        for i in range(hi):
            if i not in seen:
                ans = bin(i)[2:]
                return "0" * (n - len(ans)) + ans
            
        return ""
