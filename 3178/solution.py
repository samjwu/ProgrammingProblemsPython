class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        max_idx = n - 1

        trips = k // max_idx
        remaining_steps = k % max_idx

        if trips % 2 == 0:
            # round trip
            return remaining_steps
        else:
            # return trip
            return max_idx - remaining_steps
