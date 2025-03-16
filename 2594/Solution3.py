class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        freq = Counter(ranks)

        # min heap storing 
        # (repair time, mechanic rank, repair count, freq of mechanic rank)
        # init repair time = rank * 1 * 1 = rank
        min_heap = [[rank, rank, 1, freq[rank]] for rank in freq]
        heapify(min_heap)

        # Process until all cars are repaired
        while cars > 0:
            # get mechanic rank that is able to repair the next car soonest
            repair_time, rank, repair_count, rank_freq = heappop(min_heap)

            # each mechanic in this rank repairs a car
            cars -= rank_freq

            # increment repair count for mechanic rank
            repair_count += 1

            heappush(min_heap, [rank * repair_count * repair_count, rank, repair_count, rank_freq])

        return repair_time
