class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # map source (0-indexed) to possible destinations
        moves = {
            0:(1, 3),
            1:(0, 2, 4),
            2:(1, 5),
            3:(0, 4),
            4:(1, 3, 5),
            5:(2, 4)
        }

        # convert board to string
        state = "".join(str(c) for c in board[0] + board[1])

        # can only move starting from empty square
        start = state.index('0')

        visited = set()

        # store (position, board state, steps taken)
        queue = collections.deque([(start, state, 0)])

        # bfs
        while queue:
            position, state, steps = queue.popleft()

            if state == "123450":
                return steps
            elif state in visited:
                continue
            else:
                visited.add(state)

                for move in moves[position]:
                    newState = list(state)
                    newState[position], newState[move] = newState[move], newState[position]
                    newState = "".join(newState)
                    queue.append((move, newState, steps + 1))

        return -1
