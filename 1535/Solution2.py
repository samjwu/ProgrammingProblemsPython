class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_element = max(arr)
        
        curr_max = arr[0]
        queue = deque(arr[1:])
        
        wins = 0

        while queue:
            compare = queue.popleft()
            
            if curr_max > compare:
                queue.append(compare)
                wins += 1
            else:
                queue.append(curr_max)
                curr_max = compare
                wins = 1
            
            if wins == k or curr_max == max_element:
                return curr_max
