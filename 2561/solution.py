from collections import Counter
from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # use single counter for fruit price frequency
        # positive => more in basket 1
        # negative => more in basket 2
        # 0 => equal count of fruits with that price
        prices = Counter(basket1)
        for price in basket2:
            prices[price] -= 1

        # store prices of fruits that must be swapped
        swaps = []

        for price, fruits in prices.items():
            # if number of fruits with same price is odd, there is no valid answer
            if fruits % 2 != 0:
                return -1

            # number of swaps is half the number of fruits
            # add the price for each swap
            swaps.extend([price] * abs(fruits // 2))
        
        # use the cheapest fruit for swaps to minimize cost
        min_price = min(basket1 + basket2)
        
        # since cost is min(basket1[i], basket2[j])
        # sort the swaps to use the first half which is cheaper
        swaps.sort()
        
        # use the first half of the swaps
        # for each swap, there are two options. take the min
        # 1. directly swap the fruit (A and B)
        #     => cost is price for that fruit
        # 2. swap the fruit (A) with the cheapest,
        #     then swap cheapest again with another fruit (B)
        #     => cost is cheapest fruit price * 2
        return sum(min(price, min_price * 2) for price in swaps[0:len(swaps)//2])
