class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        ans = set()
        used = [False for _ in range(n)]

        self.recurse(tiles, "", used, ans)

        # recurse included empty string
        # so return all answers minus 1
        return len(ans) - 1

    def recurse(self, tiles: str, current: str, used: list, ans: set) -> None:
        ans.add(current)

        for i, c in enumerate(tiles):
            if not used[i]:
                used[i] = True
                self.recurse(tiles, current + c, used, ans)
                # backtrack
                used[i] = False
