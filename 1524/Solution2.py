class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 1e9 + 7
        ans = 0

        prefix_sum = 0
        
        # track number of odd and even subarrays
        # starting from 0th index (exclusive)
        odd_count = 0
        # initial sum is 0, so init even count to 1
        even_count = 1

        # update answer while updating prefix sum
        for num in arr:
            prefix_sum += num

            # to construct odd sum subarrays,
            # remove all opposite parity subarrays starting from 0
            # the odd and even counts keep track of this number
            if prefix_sum % 2 == 0:
                # odd (prev) + even (curr) = odd
                # current prefix is even
                # opposite parity is odd
                ans += odd_count
                even_count += 1
            else:
                # even (prev) + odd (curr) = odd
                # current prefix is odd
                # opposite parity is even
                ans += even_count
                odd_count += 1

            ans %= MOD

        return int(ans)
