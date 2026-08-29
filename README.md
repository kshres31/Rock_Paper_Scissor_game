# Rock Paper Scissors

A terminal-based Rock Paper Scissors game written in Python. Play against the computer, track your score across multiple rounds, and see your final match results.

## Features

- Player vs computer gameplay
- Random computer move selection
- Input validation (accepts words, numbers 1-3, and shorthand R/P/S)
- Case-insensitive and whitespace-tolerant input
- Score tracking across multiple rounds
- Win streak tracking with fire emoji at 3+ wins
- Win percentage and best streak in final summary
- In-game rules display (? key)
- Clean terminal UI
- Replay support — play as many rounds as you want

## Rules

```
Rock beats Scissors
Scissors beats Paper
Paper beats Rock
Same choices result in a draw
```

## How to Run

```bash
python main.py
```

## How to Play

1. Run the game with `python main.py`
2. Choose your move by typing:
   - A number: `1` (Rock), `2` (Paper), `3` (Scissors)
   - A word: `rock`, `paper`, or `scissors`
   - A shorthand letter: `R`, `P`, or `S`
   - `Q` to quit
   - `?` to view rules
3. The computer picks a random move
4. The winner is displayed along with the current score
5. Choose to play another round or quit

## Example

```
========================================
       ROCK PAPER SCISSORS
========================================

Choose your move:

  1. Rock
  2. Paper
  3. Scissors
  ?. Rules
  Q. Quit

Your choice: rock

You chose:      Rock
Computer chose: Scissors

Rock beats Scissors!
You win!

----------------------------------------
Score
You: 1
Computer: 0
Draws: 0
----------------------------------------

Play another round? (y/n):
```

## Project Structure

```
rock-paper-scissors/
├── main.py          # Game loop, UI, and entry point
├── game.py          # Core game logic (choices, winner, input)
├── README.md
├── .gitignore
└── tests/
    ├── __init__.py
    └── test_game.py  # Unit tests for game logic
```

## Running Tests

```bash
python -m unittest discover -s tests -v
```

## What I Learned

- Writing clean Python functions with clear responsibilities
- Input validation and error handling without crashes
- Using `random.choice` for computer selection
- Dictionary-based lookup for game logic
- Unit testing with Python's `unittest` module
- Organizing code across multiple files
- Building a simple but readable terminal interface
