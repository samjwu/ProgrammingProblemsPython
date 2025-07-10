from collections import defaultdict
from typing import List

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1

        dupe_xor = 0

        for num in freq:
            if freq[num] == 2:
                dupe_xor ^= num

        return dupe_xor
