class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def recurse(s: str) -> str:
            if len(s) == n:
                if s not in nums:
                    return s
                return ""
            
            # try adding zero
            zero = recurse(s + "0")
            if zero:
                return zero

            # try adding one
            return recurse(s + "1")

        n = len(nums)
        nums = set(nums)
        return recurse("")
