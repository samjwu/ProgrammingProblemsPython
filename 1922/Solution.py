class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def fast_expo(base: int, exponent: int) -> int:
            ans = 1
            multiplier = base

            while exponent > 0:
                if exponent % 2 == 1:
                    ans = ans * multiplier % MOD
                multiplier = multiplier * multiplier % MOD
                exponent //= 2

            return ans

        # (n+1)//2 even indices, 5 even numbers => 5^((n+1)//2)
        # n//2 odd indices, 4 primes => 4^(n//2)
        return fast_expo(5, (n + 1) // 2) * fast_expo(4, n // 2) % MOD
