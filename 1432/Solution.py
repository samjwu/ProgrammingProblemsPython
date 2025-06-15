class Solution:
    def maxDiff(self, num: int) -> int:
        min_val = num
        max_val = num
        
        for x in range(10):
            for y in range(10):
                changed = str(num).replace(str(x), str(y))
                if changed[0] != "0":
                    changed_val = int(changed)
                    min_val = min(min_val, changed_val)
                    max_val = max(max_val, changed_val)

        return max_val - min_val
