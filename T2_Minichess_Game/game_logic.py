from utils import check_for_checkmate, check_for_stalemate

class GameLogic:
    def __init__(self, board):
        self.board = board

    def start_game(self, players):
        """Start the game and handle alternating turns."""
        turn = 0
        while True:
            current_player = players[turn % len(players)]
            self.board.display()

            while True:
                try:
                    # Get move from player
                    start, end = current_player.make_move(self.board)

                    # Validate move
                    if not self.board.is_valid_move(start, end):
                        print("Invalid move. Try again.")
                        continue

                    # Apply move
                    self.board.make_move(start, end)
                    break  # move successful

                except ValueError as ve:
                    print(f"Move Error: {ve}. Try again.")
                except Exception as e:
                    print(f"Unexpected Error: {e}. Try again.")

            # Check for end-game conditions
            if check_for_checkmate(self.board, current_player.color):
                print(f"{current_player.name} wins by Checkmate!")
                break
            if check_for_stalemate(self.board):
                print("It's a Stalemate!")
                break

            turn += 1
