class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        
        ans = 0
        
        idx = 0
        
        while tickets[k] > 0:
            while tickets[idx] == 0:
                idx = (idx + 1) % n
                
            tickets[idx] -= 1
            idx = (idx + 1) % n
            ans += 1
            
        return ans
