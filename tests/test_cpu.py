import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'T2_Minichess_Game')))

from player import CPU
from board import Board


def test_cpu_move_returns_valid_indices():
    cpu = CPU("CPU", "B")
    board = Board()
    move = cpu.make_move(board)
    assert isinstance(move, tuple)
    assert isinstance(move[0], tuple)
    assert isinstance(move[1], tuple)
