# Data Model Design (T1 - Minichess)

## 1. Overview
This document defines and justifies the data models for the Minichess simulator using **Set Theory**, with corresponding type definitions in **Python**.

---

## 2. Set Theory Definitions

### A. Chessboard
- A 6x6 matrix representing the game board.

**Set Definition**:
```
Board ∈ Position → (Piece ∪ Empty)
Position = { (x, y) | x ∈ {1..6}, y ∈ {1..6} }
```

### B. Pieces
```
Piece = {King, Queen, Rook, Bishop, Knight, Pawn}
Color = {White, Black}
```

Each piece is uniquely identified by type and color:
```
PieceInstance = Piece × Color
```

---

## 3. Python Type Definitions

```python
from enum import Enum
from typing import Optional, Tuple, List

class PieceType(Enum):
    KING = 'K'
    QUEEN = 'Q'
    ROOK = 'R'
    BISHOP = 'B'
    KNIGHT = 'N'
    PAWN = 'P'

class Color(Enum):
    WHITE = 'W'
    BLACK = 'B'

class Piece:
    def __init__(self, type: PieceType, color: Color):
        self.type = type
        self.color = color

Position = Tuple[int, int]  # (row, column)
Board = List[List[Optional[Piece]]]  # 6x6 grid
```

---

## 4. Game State Model

```
GameState = {
    'board': Board,
    'turn': Color,
    'status': GameStatus,
    'winner': Optional[Color]
}
```

```python
class GameStatus(Enum):
    ONGOING = 0
    CHECKMATE = 1
    STALEMATE = 2
```

---

## 5. Move Representation

```
Move = Position × Position
```

```python
class Move:
    def __init__(self, start: Position, end: Position):
        self.start = start
        self.end = end
```

---

## 6. Justification

- **Set Theory** allows clear formal definition of game components.
- **Enum & Object-Oriented modeling** in Python ensures strong typing, immutability (if required), and maintainability.
- Data models are extensible to support new rules or GUI variants later.

---

## 7. Conclusion

The design ensures clarity in program state representation, maintains turn-based logic, and simplifies game logic with functional and class-based separation.
