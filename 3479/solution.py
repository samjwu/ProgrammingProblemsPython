from math import ceil, sqrt
from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)

        # square root decomposition
        # divide problem into buckets
        # make bucket size roughly equal to square root of total number of items
        bucket_size = int(ceil(sqrt(n)))

        # each bucket is a list of baskets and index of the basket
        buckets = [[] for i in range(bucket_size)]

        # group baskets by index to make searching nearby baskets faster
        for i, basket in enumerate(baskets):
            bucket_idx = i // bucket_size
            buckets[bucket_idx].append((basket, i))

        for bucket in buckets:
            bucket.sort()

        unplaced = 0
        
        for fruit in fruits:
            for bucket in buckets:
                # check if largest bucket can carry all the fruit
                # largest bucket is last bucket due to ascending sort
                if bucket and bucket[-1][0] >= fruit:
                    # to break tie breaks (two baskets with same capacity),
                    # pick the lowest index basket
                    used_basket = min((i, basket) for basket, i in bucket if basket >= fruit)
                    # remove the used basket from bucket to avoid reusing it
                    bucket.remove((used_basket[1], used_basket[0]))
                    break
            else:
                unplaced += 1

        return unplaced
