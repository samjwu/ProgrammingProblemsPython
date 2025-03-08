class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        white = 0
        ans = float("inf")
        left = 0

        # sliding window
        for right in range(n):
            if blocks[right] == "W":
                white += 1

            if right - left + 1 == k:
                ans = min(ans, white)

                if blocks[left] == "W":
                    white -= 1

                left += 1

        return ans
