class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        
        for i in range(1, n + 1):
            square = i * i
            s = str(square)

            # create memo for each string
            # memo[idx][cur] = true if valid partition can be made
            # at idx with sum cur so far
            memo = [[-1 for _ in range(i+1)] for _ in range(len(s))]

            if self.valid_partition(0, 0, s, i, memo):
                ans += square

        return ans

    def valid_partition(self, start, curr, s, target, memo):
        if start == len(s):
            return curr == target

        if curr > target:
            return False

        if memo[start][curr] != -1:
            return memo[start][curr] == 1

        valid_partition = False

        for idx in range(start, len(s)):
            t = s[start:idx + 1]
            remain = int(t)

            valid_partition = valid_partition or self.valid_partition(
                idx + 1,
                curr + remain,
                s,
                target,
                memo,
            )

            if valid_partition:
                memo[start][curr] = 1
                return True

        memo[start][curr] = 0
        return False
