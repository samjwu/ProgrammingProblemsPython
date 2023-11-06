from sortedcontainers import SortedSet

class SeatManager:
    def __init__(self, n: int):
        self.not_reserved = 1
        self.seats = SortedSet()

    def reserve(self) -> int:
        if self.seats:
            return self.seats.pop(0)

        open_seat = self.not_reserved
        self.not_reserved += 1
        return open_seat

    def unreserve(self, seat_number: int) -> None:
        self.seats.add(seat_number)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
