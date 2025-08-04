from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # only ever allow two fruits (keys) at a time
        basket = dict()
        n = len(fruits)
        
        total = 0

        # use sliding window
        left = 0
        right = 0
        
        while right < n:
            # extend window
            if fruits[right] not in basket:
                basket[fruits[right]] = 1
            else:
                basket[fruits[right]] += 1
            right += 1
            
            # shrink window if too many fruit types
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    basket.pop(fruits[left])
                left += 1
            
            total = max(total, right - left)
            
        return total
