class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 1e9 + 7
        n = len(arr)

        # convert to parity (odd/even)
        for i in range(n):
            arr[i] %= 2

        # prefix_even[i] = num even subarrays ending at i
        prefix_even = [0] * n
        # prefix_odd[i] = num odd subarrays ending at i
        prefix_odd = [0] * n

        if arr[0] % 2 == 0:
            prefix_even[0] = 1
        else:
            prefix_odd[0] = 1

        for i in range(1, n):
            if arr[i] % 2 == 1:
                # odd (curr) + even (prev) = odd (next)
                prefix_odd[i] = (1 + prefix_even[i - 1]) % MOD
                # odd (curr) + odd (prev) = even (next)
                prefix_even[i] = prefix_odd[i - 1]
            else:
                # even (curr) + even (prev) = even (next)
                prefix_even[i] = (1 + prefix_even[i - 1]) % MOD
                # even (curr) + odd (prev) = odd (next)
                prefix_odd[i] = prefix_odd[i - 1]

        return int(sum(prefix_odd) % MOD)
