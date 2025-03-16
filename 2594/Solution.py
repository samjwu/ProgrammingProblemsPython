class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # find min and max rank
        min_rank = min(ranks)
        max_rank = max(ranks)
        
        # count frequency of ranks
        freq = [0] * (max_rank + 1)

        for rank in ranks:
            freq[rank] += 1

        # binary search on min and max time needed
        low = 1
        high = min_rank * cars * cars

        while low < high:
            mid = (low + high) // 2

            repaired = 0
            for rank in range(1, max_rank + 1):
                repaired += freq[rank] * int(math.sqrt(mid // rank))

            if repaired >= cars:
                # repaired enough, can try lower time
                high = mid
            else:
                # did not repair enough, must try higher tiem
                low = mid + 1

        return low
