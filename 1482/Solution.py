class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        
        if m * k > n:
            return -1

        ans = -1
        
        left = 0
        right = max(bloomDay)

        while left <= right:
            mid = left + (right - left) // 2

            if self.countBouquets(bloomDay, mid, k) >= m:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
    
    def countBouquets(self, bloomDay: List[int], day: int, bouquetSize: int) -> int:
        bouquets = 0
        
        flowers = 0
        
        for bloom in bloomDay:
            if bloom <= day:
                flowers += 1
            else:
                flowers = 0
                
            if flowers == bouquetSize:
                bouquets += 1
                flowers = 0
                
        return bouquets
