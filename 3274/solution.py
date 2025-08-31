class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def calc_coordinate_sum(coordinate: str) -> int:
            return ord(coordinate[0]) - ord('a') + ord(coordinate[1]) - ord('1')

        return calc_coordinate_sum(coordinate1) % 2 == calc_coordinate_sum(coordinate2) % 2
