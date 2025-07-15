class Solution:
    def minimumChairs(self, s: str) -> int:
        n = len(s)
        chairs_needed = 0
        chairs_free = 0

        for i in range(n):
            if s[i] == 'E':
                if chairs_free > 0:
                    chairs_free -=1
                else:
                    chairs_needed += 1
            else:
                chairs_free += 1
        
        return chairs_needed
