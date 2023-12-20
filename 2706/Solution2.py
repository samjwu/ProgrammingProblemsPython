class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        n = len(prices)
        
        lo = min(prices[0], prices[1])
        lo2 = max(prices[0], prices[1])

        for i in range(2, n):
            if prices[i] < lo:
                lo2 = lo
                lo = prices[i]
            elif prices[i] < lo2:
                lo2 = prices[i]
            
        cost = lo + lo2

        if cost <= money:
            return money - cost
        
        return money
