from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        unplaced = 0

        for fruit in fruits:
            for i in range(n):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    break
            else:
                unplaced += 1

        return unplaced
