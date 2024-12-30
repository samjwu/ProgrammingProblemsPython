class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        self.MOD = int(1e9+7)
        memo = {}

        def recurse(cur):
            if cur > high:
                return 0

            if cur == high:
                return 1

            if cur in memo:
                return memo[cur]

            cnt = 0
            if low <= cur <= high:
                cnt += 1
            cnt += recurse(cur + zero)
            cnt += recurse(cur + one)
            cnt %= self.MOD

            memo[cur] = cnt
            return cnt

        return recurse(0)
