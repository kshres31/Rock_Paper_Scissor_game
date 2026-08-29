"""
Rock Paper Scissors — game logic.

Contains the core functions for a single round:
choice selection, computer selection, and winner determination.
"""

import random

# Valid choices and their canonical names
CHOICES = ("rock", "paper", "scissors")

# Maps each choice to what it beats
BEATS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

# Number-to-choice mapping for numeric input
NUMBER_MAP = {
    "1": "rock",
    "2": "paper",
    "3": "scissors",
}

# Shorthand letter mapping
LETTER_MAP = {
    "r": "rock",
    "p": "paper",
    "s": "scissors",
}


def get_computer_choice() -> str:
    """Return a random choice for the computer."""
    return random.choice(CHOICES)


def normalize_input(raw: str) -> str | None:
    """
    Normalize player input to a valid choice or None if invalid.

    Accepts:
      - numbers 1/2/3 (mapped to rock/paper/scissors)
      - rock / paper / scissors (any case, with whitespace stripped)
    """
    value = raw.strip().lower()

    if not value:
        return None

    if value in NUMBER_MAP:
        return NUMBER_MAP[value]

    if value in LETTER_MAP:
        return LETTER_MAP[value]

    if value in CHOICES:
        return value

    return None


def determine_winner(player: str, computer: str) -> str:
    """
    Determine the result of a round.

    Returns:
      "player"  — player wins
      "computer" — computer wins
      "draw"    — same choice
    """
    if player == computer:
        return "draw"

    if BEATS[player] == computer:
        return "player"

    return "computer"


def describe_round(player: str, computer: str, result: str) -> str:
    """
    Return a human-readable description of a round's outcome.
    """
    if result == "draw":
        return f"Both chose {player.capitalize()} — it's a draw!"

    winner_choice = player if result == "player" else computer
    loser_choice = computer if result == "player" else player
    winner_label = "You" if result == "player" else "Computer"

    return f"{winner_choice.capitalize()} beats {loser_choice.capitalize()}!\n{winner_label} win{'s' if result == 'computer' else ''}!"
