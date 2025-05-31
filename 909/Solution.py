class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def square_to_board(square: int) -> (int, int):
            """
            Convert square position to board position
            (square number to row and column)

            For a Boustrophedon board
            eg:
            7 8 9
            6 5 4
            1 2 3
            """
            r = (square - 1) // n
            c = (square - 1) % n

            # since the board is Boustrophedon
            # for even rows use the col value
            # for odd rows use the inverted col value
            if r % 2 == 0:
                return n-1-r, c
            else:
                return n-1-r, n-1-c
            
        queue = collections.deque()
        queue.append((1, 0))
        seen = set()
        seen.add(1)

        while queue:
            square, moves = queue.popleft()
            r, c = square_to_board(square)

            # snake or ladder
            if board[r][c] != -1:
                square = board[r][c]

            if square == n * n:
                return moves

            # try all dice rolls
            for x in range(1, 7):
                new_square = square + x
                if new_square <= n * n and new_square not in seen:
                    seen.add(new_square)
                    queue.append((new_square, moves + 1))

        return -1
