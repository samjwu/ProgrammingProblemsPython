class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 1. If any bit flips at position i in the range [left, right],
        # the bitwise AND of the entire column is 0
        
        # 2. All columns to the right of the flipped bit are also 0
        
        # From 1/2, rangeBitwiseAnd is just
        # the common prefix of left and right

        shifts = 0
    
        while left != right:
            left = left >> 1
            right = right >> 1
            shifts += 1
        
        return right << shifts
