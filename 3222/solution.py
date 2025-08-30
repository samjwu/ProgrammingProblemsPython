class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        picks = min(x, y // 4)

        if picks % 2 == 0:
            return "Bob"
        return "Alice"
