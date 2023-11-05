class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_element = max(arr)
        
        curr_max = arr[0]
        
        wins = 0

        for i in range(1, len(arr)):
            compare = arr[i]
            
            if curr_max > compare:
                wins += 1
            else:
                curr_max = compare
                wins = 1
            
            if wins == k or curr_max == max_element:
                return curr_max
