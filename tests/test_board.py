import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'T2_Minichess_Game')))

import pytest
from board import Board

def test_board_initialization():
    board = Board()
    assert board.board[0][0] == 'r'
    assert board.board[7][4] == 'K'
    assert board.board[3][3] == '.'

def test_make_move_success():
    board = Board()
    board.make_move((6, 0), (5, 0))  # P from a2 to a3
    assert board.board[5][0] == 'P'
    assert board.board[6][0] == '.'

def test_make_move_invalid_empty_start():
    board = Board()
    with pytest.raises(ValueError):
        board.make_move((4, 4), (3, 4))  # No piece

def test_make_move_invalid_capture_same_color():
    board = Board()
    with pytest.raises(ValueError):
        board.make_move((7, 1), (7, 2))  # N captures B, both white
