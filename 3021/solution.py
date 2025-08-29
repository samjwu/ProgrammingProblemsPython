class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Alice wins when x + y is odd
        # there are n * m possible pairs
        # half of these pairs have odd sum
        # when both n and m are odd, subtract 1 possibility because n + m is odd
        return (n * m) // 2
