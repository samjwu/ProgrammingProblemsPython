class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        memo = {}
        
        # add one for paste op to populate board
        return self.recurse(1, 1, n, memo) + 1
        
    def recurse(self, board: int, curr: int, target: int, memo: dict[tuple, int]) -> int:
        if curr == target:
            return 0
        
        if curr > target:
            return 1001
        
        if (board, curr) in memo:
            return memo[(board, curr)]
        
        # 1 copy current string op + 1 paste op = 2 ops
        copyPaste = self.recurse(curr, curr * 2, target, memo) + 2
        paste = self.recurse(board, curr + board, target, memo) + 1
        
        memo[(board, curr)] = min(copyPaste, paste)
        
        return memo[(board, curr)]
