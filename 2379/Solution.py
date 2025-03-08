from collections import deque

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        q = deque()
        white = 0

        for i in range(k):
            curr = blocks[i]
            q.append(curr)

            if curr == "W":
                white += 1

        ans = white

        for i in range(k, n):
            if q.popleft() == "W":
                white -= 1

            curr = blocks[i]
            q.append(curr)

            if curr == "W":
                white += 1

            ans = min(ans, white)

        return ans
