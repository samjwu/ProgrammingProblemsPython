class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            # edge case: upper bound of prime is element itself for 1st
            if i == 0:
                bound = nums[0]
            else:
                # upper bound of prime is diff of curr and prev
                bound = nums[i] - nums[i - 1]

            # assuming nums[0] >= 0
            # detected array is not strictly increasing
            if bound <= 0:
                return False

            largestPrime = 0
            for j in range(bound - 1, 1, -1):
                if self.isPrime(j):
                    largestPrime = j
                    break

            nums[i] = nums[i] - largestPrime

        return True

    def isPrime(self, num: int) -> bool:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False

        return True
