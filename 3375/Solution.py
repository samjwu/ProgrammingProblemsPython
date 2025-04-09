class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        reduced = set()

        for num in nums:
            if num > k:
                # can reduce all of same num to k
                reduced.add(num)
            elif num < k:
                # cannot increase to k
                return -1

        return len(reduced)
