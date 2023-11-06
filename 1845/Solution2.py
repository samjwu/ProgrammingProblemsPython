class SeatManager:
    def __init__(self, n: int):
        self.not_reserved = 1
        
        # python heapq uses minheap by default
        self.seats = []

    def reserve(self) -> int:
        if self.seats:
            return heapq.heappop(self.seats)

        open_seat = self.not_reserved
        self.not_reserved += 1
        return open_seat

    def unreserve(self, seat_number: int) -> None:
        heapq.heappush(self.seats, seat_number)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
