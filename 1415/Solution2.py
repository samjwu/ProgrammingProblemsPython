class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.curr = ""
        self.ans = ""
        self.idx = 0

        self.recurse(n, k)

        return self.ans

    def recurse(self, n: int, k: int) -> None:
        if len(self.curr) == n:
            self.idx += 1

            if self.idx == k:
                self.ans = self.curr

            return

        for c in "abc":
            # skip duplicate chars
            if len(self.curr) > 0 and self.curr[-1] == c:
                continue

            self.curr += c

            self.recurse(n, k)

            if self.ans != "":
                return

            # backtrack
            self.curr = self.curr[:-1]
