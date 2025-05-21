import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'T2_Minichess_Game')))

from board import Board
from game_logic import GameLogic
from player import Player


def test_game_logic_initialization():
    board = Board()
    logic = GameLogic(board)
    assert logic.board is board
