class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(board, i, j, word, 0):
                    return True
                
        return False
    
    def dfs(self, board: List[List[str]], i: int, j: int, word: str, idx: int) -> bool:
        if idx == len(word):
            return True
        
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return False
        
        if board[i][j] != word[idx]:
            return False
        
        board[i][j] = "#"
        
        ans = self.dfs(board, i+1, j, word, idx+1) \
            or self.dfs(board, i-1, j, word, idx+1) \
            or self.dfs(board, i, j+1, word, idx+1) \
            or self.dfs(board, i, j-1, word, idx+1)
        
        board[i][j] = word[idx]
        
        return ans
