from collections import defaultdict

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = defaultdict(int)

        for num in arr:
            freq[num] += 1

        lucky = -1

        for num in freq:
            if num == freq[num]:
                lucky = max(lucky, num)

        return lucky
