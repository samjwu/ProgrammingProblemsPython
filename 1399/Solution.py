class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = collections.Counter()

        for i in range(1, n + 1):
            digits_sum = sum([int(digit) for digit in str(i)])
            groups[digits_sum] += 1
        
        high = max(groups.values())
        ans = sum(1 for v in groups.values() if v == high)
        
        return ans
