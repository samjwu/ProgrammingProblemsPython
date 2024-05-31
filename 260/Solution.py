class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # equivalent to XOR of element 1 and 2
        xorAll = 0
        
        for num in nums:
            xorAll ^= num
        
        # any '1' in the XOR of 1 and 2
        # is a bit in which they are different
        
        # bitwise AND of a number and its 2s complement
        # returns the rightmost bit
        rightmostDiffBit = xorAll & -xorAll
        
        element1 = 0
        element2 = 0
        
        for num in nums:
            if (num & rightmostDiffBit) == 0:
                element1 ^= num
            else:
                element2 ^= num
                
        return [element1, element2]
