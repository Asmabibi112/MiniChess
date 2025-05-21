class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        """Initializes the board to the starting position."""
        return [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

    def display(self):
        """Print the current board state."""
        for row in self.board:
            print(' '.join(row))
        print("\n")

    def make_move(self, start, end):
        """Move a piece from start to end if valid, otherwise raise error."""
        x1, y1 = start
        x2, y2 = end

        piece = self.board[x1][y1]

        if piece == ".":
            raise ValueError("No piece at the starting position.")

        if self.board[x2][y2] != "." and self.is_same_color(piece, self.board[x2][y2]):
            raise ValueError("Cannot capture your own piece.")

        self.board[x2][y2] = piece
        self.board[x1][y1] = "."

    def is_same_color(self, piece1, piece2):
        """Check if both pieces are of the same color."""
        return (piece1.isupper() and piece2.isupper()) or (piece1.islower() and piece2.islower())

    def is_valid_move(self, start, end):
        """
        Placeholder: Validate if a move is legal according to basic rules.
        Currently always returns True.
        """
        return True

    def algebraic_to_index(self, pos):
        """
        Convert algebraic notation like 'a2' to matrix indices.
        'a1' -> (7, 0), 'h8' -> (0, 7)
        """
        col_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        if len(pos) != 2 or pos[0] not in col_map or not pos[1].isdigit():
            raise ValueError(f"Invalid algebraic notation: {pos}")
        row = 8 - int(pos[1])  # '1' => 7, '8' => 0
        col = col_map[pos[0]]
        return row, col
