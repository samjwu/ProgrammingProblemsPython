class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist1 = abs(z - x)
        dist2 = abs(z - y)

        if dist1 == dist2:
            return 0
        elif dist1 < dist2:
            return 1
        return 2
