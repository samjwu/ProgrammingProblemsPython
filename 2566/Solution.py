class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        min_val = float('inf')
        max_val = float('-inf')

        for from_digit in '0123456789':
            for to_digit in '0123456789':
                if from_digit == to_digit:
                    continue

                remapped = s.replace(from_digit, to_digit)

                val = int(remapped)
                min_val = min(min_val, val)
                max_val = max(max_val, val)

        return max_val - min_val
