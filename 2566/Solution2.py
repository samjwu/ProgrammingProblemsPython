class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_val = str(num)
        min_val = max_val
        idx = 0
        n = len(max_val)

        while idx < n and max_val[idx] == "9":
            idx += 1

        if idx < n:
            max_val = max_val.replace(max_val[idx], "9")

        min_val = min_val.replace(min_val[0], "0")
        
        return int(max_val) - int(min_val)
