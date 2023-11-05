class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        if k >= n:
            return max(arr)
        
        ans = max(arr[0], arr[1])
        winner = ans
        wins = 1
        
        arr.remove(min(arr[0], arr[1]))
        arr.append(min(arr[0], arr[1]))
        
        while wins < k:
            winner = max(arr[0], arr[1])
            
            if winner == ans:
                wins += 1
            else:
                wins = 1
                ans = winner
            
            arr.remove(min(arr[0], arr[1]))
            arr.append(min(arr[0], arr[1]))
            
        return ans
        