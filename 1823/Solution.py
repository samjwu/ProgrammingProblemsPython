class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i+1 for i in range(n)]
        
        idx = 0
        
        while len(friends) > 1:
            idx = (idx + k-1) % len(friends)
            friends.pop(idx)
            
        return friends[0]
