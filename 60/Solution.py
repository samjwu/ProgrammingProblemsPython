class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        # convert to 0-based index
        k -= 1
        kth_perm = []

        for i in range(n):
            # block size: (len(nums) - 1)! permutations
            # equivalent to  (n-1-i)! permutations
            fact = math.factorial(n - 1 - i)
            # block index: the digit to pick from left to right at ith step
            index = k // fact
            kth_perm.append(nums.pop(index))
            # update k to current position in block
            k %= fact

        return ''.join(kth_perm)
