from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        remainder_freq = [0] * 24
        day_pairs = 0

        for hour in hours:
            remainder = hour % 24

            if remainder == 0:
                day_pairs += remainder_freq[0]
            else:
                day_pairs += remainder_freq[24 - remainder]

            remainder_freq[remainder] += 1

        return day_pairs
