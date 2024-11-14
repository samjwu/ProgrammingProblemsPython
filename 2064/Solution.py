class Solution:
    def canDistrib(self, n: int, quantities: List[int], x: int) -> bool:
        idx = 0
        product = quantities[idx]

        for i in range(n):
            if product <= x:
                # distribute next product
                idx += 1
                
                if idx == len(quantities):
                    return True
                else:
                    product = quantities[idx]
            else:
                # keep distributing current product
                product -= x

        return False

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # binary search to get quantity x to distribute
        l = 0
        r = max(quantities)

        while l < r:
            m = (l + r) // 2

            if self.canDistrib(n, quantities, m):
                r = m
            else:
                l = m + 1

        return l
