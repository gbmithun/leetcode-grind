from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_coords(s):
            s -= 1
            row = n - 1 - (s // n)
            col = s % n if (n - 1 - row) % 2 == 0 else n - 1 - (s % n)
            return row, col

        visited = set()
        queue = deque([(1, 0)])

        while queue:
            s, moves = queue.popleft()
            if s == n * n:
                return moves
            for i in range(1, 7):
                next_s = s + i
                if next_s > n * n:
                    continue
                r, c = get_coords(next_s)
                if board[r][c] != -1:
                    next_s = board[r][c]
                if next_s not in visited:
                    visited.add(next_s)
                    queue.append((next_s, moves + 1))
        return -1
