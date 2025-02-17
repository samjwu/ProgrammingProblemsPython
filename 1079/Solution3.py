class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seen = set()

        sorted_tiles = "".join(sorted(tiles))

        return self.recurse(sorted_tiles, "", 0, seen) - 1

    def recurse(self, tiles: str, curr: str, i: int, seen: set) -> int:
        if i >= len(tiles):
            # found new unique sequence
            if curr not in seen:
                seen.add(curr)
                # count perms for new unique sequence
                return self.permutations(curr)
            return 0

        # try candidate sequences by excluding or including next char
        exclude = self.recurse(tiles, curr, i + 1, seen)
        include = self.recurse(tiles, curr + tiles[i], i + 1, seen)
        return exclude + include

    def permutations(self, seq: str) -> int:
        ans = self.factorial(len(seq))

        # divide by factorial of each char frequency
        for count in Counter(seq).values():
            ans //= self.factorial(count)

        return ans

    def factorial(self, n: int) -> int:
        if n <= 1:
            return 1

        ans = 1
        for num in range(2, n + 1):
            ans *= num

        return ans
