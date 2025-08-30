from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # track numbers seen in each row, column, and box
        row_groups = defaultdict(set)
        col_groups = defaultdict(set)
        box_groups = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                # if number was already seen in a previous group
                # then board is invalid
                if (
                    board[i][j] in row_groups[i]
                    or board[i][j] in col_groups[j]
                    or board[i][j] in box_groups[(i // 3, j // 3)]
                ):
                    return False

                row_groups[i].add(board[i][j])
                col_groups[j].add(board[i][j])
                box_groups[(i // 3, j // 3)].add(board[i][j])

        return True
