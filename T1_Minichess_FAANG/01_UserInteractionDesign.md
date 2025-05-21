# User Interaction Design (T1 - Minichess)

## 1. Overview
This document describes how users will interact with the Minichess command line simulator using Gherkin specifications based on Hoare Logic principles.

---

## 2. Interaction Flow

### a. Game Startup

```gherkin
Feature: Game Startup
  Scenario: Starting the game
    Given the user has launched the Minichess simulator
    When the user selects "New Game"
    Then the program should prompt for game type selection (2-player or CPU)
```

**Hoare Logic**  
Precondition: `program_started = True`  
Postcondition: `display_menu = True`

---

### b. Selecting Game Mode

```gherkin
Feature: Select Game Mode
  Scenario: Player selects 2-player game
    Given the menu is displayed
    When the user selects "2-Player Game"
    Then the board is initialized and Player 1 is prompted to move
```

**Hoare Logic**  
Pre: `menu_displayed = True`  
Post: `game_mode = multiplayer AND board_initialized = True`

---

### c. Making a Move

```gherkin
Feature: Move Piece
  Scenario: Player moves a valid piece
    Given it's the player's turn and a valid move is selected
    When the move is input
    Then the board updates and the turn switches
```

**Hoare Logic**  
Pre: `valid_move = True`  
Post: `board_updated = True AND turn_switched = True`

---

### d. Winning Condition

```gherkin
Feature: Winning the Game
  Scenario: Player captures opponent king
    Given a move results in capturing the king
    When the move is executed
    Then the game ends and the player is declared winner
```

**Hoare Logic**  
Pre: `king_in_checkmate = True`  
Post: `game_over = True AND winner = current_player`

---

### e. Single Player Mode

```gherkin
Feature: CPU Game
  Scenario: Player plays against CPU
    Given the user selects "Single Player Game"
    When the game starts
    Then the player goes first and CPU takes alternate turns
```

**Hoare Logic**  
Pre: `selected_mode = single_player`  
Post: `cpu_turns_enabled = True`

---

## 3. Conclusion
This interaction model ensures the game is logically consistent and user-friendly using clear Gherkin scenarios and Hoare-based validation for each interaction.

