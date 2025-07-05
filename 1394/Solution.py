from collections import defaultdict
from typing import List 

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = defaultdict(int)

        for num in arr:
            freq[num] += 1

        lucky = -1

        for num, count in freq.items():
            if num == count:
                lucky = max(lucky, num)

        return lucky
