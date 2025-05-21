import random

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color  # 'W' or 'B'

    def make_move(self, board):
        """
        Ask player for a move input and return it in (x, y) index format.
        Validates the input format and logical move feasibility.
        """
        while True:
            try:
                move = input(f"Player {self.color} (e.g., 'a2 to a3'): ").strip().lower()
                start_pos, end_pos = move.split(' to ')

                start = self.convert_to_index(start_pos)
                end = self.convert_to_index(end_pos)

                # Check board boundaries
                if not self.is_within_bounds(start) or not self.is_within_bounds(end):
                    print("Move is out of bounds. Try again.")
                    continue

                return start, end

            except ValueError:
                print("Invalid format. Please use 'a2 to a3' format.")
            except Exception as e:
                print(f"Error: {e}. Try again.")

    def convert_to_index(self, pos):
        """
        Convert chess notation (e.g., 'a2') to (row, col) index.
        """
        files = 'abcdefgh'
        if len(pos) != 2 or pos[0] not in files or not pos[1].isdigit():
            raise ValueError("Invalid position format.")
        
        col = files.index(pos[0])
        row = 8 - int(pos[1])  # Chessboard row '1' is last index
        return (row, col)

    def is_within_bounds(self, position):
        """Check if (row, col) is within 8x8 board."""
        row, col = position
        return 0 <= row < 8 and 0 <= col < 8


class CPU(Player):
    def __init__(self, name, color):
        super().__init__(name, color)

    def make_move(self, board):
        """Generate a random pseudo-legal move (placeholder)."""
        # Collect all possible starting positions for CPU's pieces
        own_pieces = 'pnbrqk' if self.color == 'B' else 'PNBRQK'
        moves = []

        for i in range(8):
            for j in range(8):
                if board.board[i][j] in own_pieces:
                    # Try moving forward 1 step if empty
                    direction = 1 if self.color == 'B' else -1
                    new_i = i + direction
                    if 0 <= new_i < 8 and board.board[new_i][j] == '.':
                        moves.append(((i, j), (new_i, j)))

        if not moves:
            raise Exception("CPU has no valid moves")

        move = random.choice(moves)
        print(f"{self.name} moves from {self.index_to_notation(move[0])} to {self.index_to_notation(move[1])}")
        return move

    def index_to_notation(self, index):
        files = 'abcdefgh'
        row, col = index
        return f"{files[col]}{8 - row}"
