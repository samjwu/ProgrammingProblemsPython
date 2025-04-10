class Solution:
    def numberOfPowerfulInt(
        self, start: int, finish: int, limit: int, s: str
    ) -> int:
        low = str(start)
        high = str(finish)
        n = len(high)
        prefix_len = n - len(s)
        
        low = low.zfill(n)

        @cache
        def dfs(i, is_limited_low, is_limited_high):
            # base case: built the powerful int
            if i == n:
                return 1

            # determine bounds of next digit
            # if limited by low, digit must be above ith char of low
            digit_low = int(low[i]) if is_limited_low else 0
            # if limited by high, digit must be below ith char of high
            digit_high = int(high[i]) if is_limited_high else 9

            ans = 0

            # in prefix part, can choose any digit
            if i < prefix_len:
                # digit just has to be within the low and high digit
                # and final answer must be below the limit
                for digit in range(digit_low, min(digit_high, limit) + 1):
                    # is_limited_low and is_limited_high remain true
                    # only if the digit exactly matches the bound
                    ans += dfs(
                        i + 1,
                        is_limited_low and digit == digit_low,
                        is_limited_high and digit == digit_high,
                    )
            else: 
                # in suffix part
                # digit should match the suffix exactly
                digit = int(s[i - prefix_len])
                # check digit is within bounds
                if digit_low <= digit <= min(digit_high, limit):
                    # same logic as when recursing on prefix
                    ans = dfs(
                        i + 1,
                        is_limited_low and digit == digit_low,
                        is_limited_high and digit == digit_high
                    )

            return ans

        return dfs(0, True, True)
