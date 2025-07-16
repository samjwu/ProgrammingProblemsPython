from typing import List

class Solution:
    def maximum_length(self, nums: List[int]) -> int:
        odd_count = 0
        even_count = 0
        alternate_count = 1
        
        prev_parity = nums[0] % 2
        
        for num in nums:
            parity = num % 2
            
            if parity:
                even_count += 1
            else:
                odd_count += 1
            
            if prev_parity != parity:
                alternate_count += 1
            
            prev_parity = parity
            
        return max(odd_count, even_count, alternate_count)
