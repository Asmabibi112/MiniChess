from board import Board
from game_logic import GameLogic
from player import Player, CPU
from utils import print_welcome, print_game_over, get_game_mode

def main():
    print_welcome()
    game_mode = get_game_mode()  # Let the user choose game mode

    board = Board()
    game_logic = GameLogic(board)

    if game_mode == "2P":
        player1 = Player("Player 1", 'W')
        player2 = Player("Player 2", 'B')
    else:  # 1-Player vs CPU
        player1 = Player("Player", 'W')
        player2 = CPU("CPU", 'B')

    players = [player1, player2]
    game_logic.start_game(players)

if __name__ == "__main__":
    main()
