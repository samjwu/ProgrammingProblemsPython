class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low = 1

        # high = cars^2 is still an upper bound
        # since it assumes only the fastest mechanic is repairing
        # even in the worst case
        high = ranks[0] * cars * cars

        while low < high:
            mid = (low + high) // 2

            repaired = sum(int(math.sqrt(mid // rank)) for rank in ranks)

            if repaired < cars:
                low = mid + 1
            else:
                high = mid

        return low
