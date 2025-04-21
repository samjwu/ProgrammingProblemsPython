class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        low = 0
        high = 0
        curr = 0

        for diff in differences:
            curr += diff
            low = min(low, curr)
            high = max(high, curr)
            
            if high - low > upper - lower:
                return 0

        return (upper - lower) - (high - low) + 1
