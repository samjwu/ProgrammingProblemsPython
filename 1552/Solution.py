class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        ans = 0
        
        n = len(position)
        
        position.sort()
        
        left = 1
        right = int(ceil((position[-1] - position[0]) / (m - 1)))
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if self.hasSolution(position, m, mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
    
    def hasSolution(self, position: List[int], balls: int, minDist: int) -> int:
        n = len(position)
        
        prev = position[0]
        
        used = 1
        
        for i in range(1, n):
            if position[i] - prev >= minDist:
                used += 1
                prev= position[i]
                
            if used == balls:
                return True
        
        return False
