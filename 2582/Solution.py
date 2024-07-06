class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        position = 1
        direction = 1
        
        while time > 0:
            position += direction
            time -= 1
            
            if position == n or position == 1:
                direction *= -1
                
        return position
