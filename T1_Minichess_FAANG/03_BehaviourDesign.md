# Behaviour Design (T1 - Minichess)

## 1. Overview
This document specifies and justifies the behaviors of the Minichess simulator using formal techniques from:
- **Mathematical Relations**
- **Mathematical Functions**
- **Graph Theory**

---

## 2. Functional Specification

### A. Turn System
We model turns as a function:
```
NextTurn: Color → Color
NextTurn(W) = B
NextTurn(B) = W
```

### B. Valid Moves

A relation between a Piece and possible Positions:
```
ValidMove ⊆ PieceInstance × Position × Position
```
Meaning: a piece of a player can move from one position to another if it's valid according to chess rules.

---

## 3. Move Validation Function

```python
def is_valid_move(board: Board, move: Move, player: Color) -> bool:
    # Check if the move is legal for the piece and board state
    pass
```

This function must satisfy:
- Only move player’s pieces.
- Destination must not have the player's own piece.
- Follow piece-specific rules.
- Not leave the king in check.

---

## 4. Game Progression: Graph Model

We define the game as a graph:
- **Nodes**: Unique game states (G)
- **Edges**: Legal moves (M)
- **Start Node**: Initial configuration
- **Terminal Nodes**: Checkmate, stalemate, or draw

```
Graph G = (V, E)
V = Set of valid board states
E = {(s₁, s₂) | s₂ = Result of applying a legal move in s₁}
```

Traversal through the graph follows legal gameplay.

---

## 5. CPU Behavior Function

The CPU’s move can be modeled as:
```
CPUMove: GameState → Move
```

```python
def cpu_select_move(game_state: GameState) -> Move:
    # Basic implementation: choose a random valid move
    pass
```

Optional: Use Minimax or heuristic if you want improved AI behavior.

---

## 6. Win Condition Relation

A function that maps game state to winner:
```
EvaluateGame: GameState → {Ongoing, WhiteWins, BlackWins, Stalemate}
```

```python
def evaluate_game(game_state: GameState) -> GameStatus:
    # Check for checkmate, stalemate, or ongoing
    pass
```

---

## 7. Summary

- Behavior is modeled with precise mathematical constructs.
- Graph theory provides a strong base for understanding state transitions.
- Functions ensure testability and encapsulate logic clearly.

---
