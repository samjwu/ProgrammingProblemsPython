class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # is_prime of Eratosthenes
        is_prime = self.sieve_of_era(right)

        primes = [num for num in range(left, right + 1) if is_prime[num]]

        if len(primes) < 2:
            return -1, -1

        min_diff = float("inf")
        ans = [-1, -1]

        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]

            if diff < min_diff:
                min_diff = diff
                ans = primes[i - 1], primes[i]

        return ans

    
    def sieve_of_era(self, hi: int) -> List[bool]:
        is_prime = [True] * (hi + 1)
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(hi**0.5) + 1):
            if is_prime[i]:
                # all multiples of primes are not prime
                for multiple in range(i * 2, hi + 1, i):
                    is_prime[multiple] = False
                    
        return is_prime
