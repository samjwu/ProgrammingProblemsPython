class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}
        r = len(ring)
        k = len(key)
        return self.recurse(0, 0, r, k, ring, key, memo)

    def calcSteps(self, curr: int, target: int, r: int) -> int:
        clockwise = abs(curr - target)
        counterClockwise = r - clockwise
        return min(clockwise, counterClockwise)

    def recurse(
        self, ringIdx: int, keyIdx: int, r: int, k: int, ring: str, key: str, memo: dict
    ) -> int:
        if (ringIdx, keyIdx) in memo:
            return memo[(ringIdx, keyIdx)]

        if keyIdx == k:
            memo[(ringIdx, keyIdx)] = 0
            return 0

        ans = inf

        for i in range(r):
            if ring[i] == key[keyIdx]:
                ans = min(
                    ans,
                    self.calcSteps(ringIdx, i, r)
                    + 1
                    + self.recurse(i, keyIdx + 1, r, k, ring, key, memo),
                )

        memo[(ringIdx, keyIdx)] = ans
        return ans
