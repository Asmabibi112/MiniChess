# CPU Design for Single-Player Mode (T1 - Minichess)

## 1. Overview
This document defines the design of the CPU (AI opponent) in single-player mode of the Minichess simulator. We implement a basic but extendable CPU player that:
- Takes valid actions.
- Attempts to respond strategically.
- Is modular enough to upgrade with smarter algorithms.

---

## 2. CPU Role in Game Loop

The CPU acts as **Player B (Black)** when a single-player game is selected. Its role is triggered right after the human player's move.

```python
if game_mode == "single_player" and current_player == "CPU":
    move = cpu_select_move(game_state)
    apply_move(move)
```

---

## 3. CPU Decision Function

A CPU move is a function:
```
CPUMove: GameState → Move
```

We begin with a **Rule-Based Random Selection**:
```python
import random

def cpu_select_move(game_state: GameState) -> Move:
    valid_moves = generate_all_valid_moves(game_state.board, player="B")
    return random.choice(valid_moves)
```

---

## 4. Heuristic-Based Move Ranking (Extension)

Optionally, we can improve the CPU with a **heuristic evaluation function**:
```python
def evaluate_board(board: Board) -> int:
    piece_values = {"K": 1000, "Q": 9, "R": 5, "B": 3, "N": 3, "P": 1}
    score = 0
    for piece in board:
        if piece.color == "W":
            score += piece_values[piece.type]
        else:
            score -= piece_values[piece.type]
    return score
```

And then:
```python
def cpu_select_move(game_state: GameState) -> Move:
    moves = generate_all_valid_moves(game_state.board, player="B")
    best_move = None
    best_score = float("inf")
    for move in moves:
        new_state = simulate_move(game_state, move)
        score = evaluate_board(new_state.board)
        if score < best_score:
            best_score = score
            best_move = move
    return best_move
```

---

## 5. Minimax Design (Advanced)

With enough time, we can implement **Minimax**:
```
Minimax: GameState × Depth → Move
```

Recursive evaluation of future moves for both players:
- Maximizing the human score.
- Minimizing CPU loss.

---

## 6. Performance Considerations

| Strategy      | Complexity | Intelligence | Suitable For |
|---------------|------------|--------------|--------------|
| Random Move   | O(n)       | ❌ Low       | Quick demo   |
| Heuristic     | O(n log n) | ✅ Medium    | Good default |
| Minimax (d=2) | O(b^d)     | ✅✅ High     | Strategic CPU |

Where `n` = # of valid moves, `b` = branching factor, `d` = search depth.

---

## 7. Summary

- The CPU module begins simple and is built for growth.
- Designed with extensibility in mind.
- Can move from random → heuristic → Minimax over time.

---
