class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        n -= 1

        trips = k // n
        remaining_steps = k % n

        if trips % 2 == 0:
            # round trip
            return remaining_steps
        else:
            # return trip
            return n - remaining_steps
