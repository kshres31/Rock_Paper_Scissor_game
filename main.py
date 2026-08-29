"""
Rock Paper Scissors — main entry point.

Run this file to play the game in your terminal.
"""

from game import (
    get_computer_choice,
    normalize_input,
    determine_winner,
    describe_round,
)

# ── Display helpers ──────────────────────────────────────────────────

DIVIDER = "=" * 40
THIN_DIVIDER = "-" * 40


def show_rules():
    """Print the game rules."""
    print(f"\n{DIVIDER}")
    print("GAME RULES".center(40))
    print(DIVIDER)
    print()
    print("  Rock beats Scissors")
    print("  Scissors beats Paper")
    print("  Paper beats Rock")
    print("  Same choice = Draw")
    print()
    print("  Input options:")
    print("    1/R = Rock")
    print("    2/P = Paper")
    print("    3/S = Scissors")
    print("    Q   = Quit")
    print()


def show_menu():
    """Print the choice menu."""
    print("\nChoose your move:\n")
    print("  1. Rock")
    print("  2. Paper")
    print("  3. Scissors")
    print("  ?. Rules")
    print("  Q. Quit")
    print("\n  (or type rock/paper/scissors)")


def show_score(wins: int, losses: int, draws: int):
    """Print the current score."""
    print(f"\n{THIN_DIVIDER}")
    print("Score")
    print(f"You: {wins}")
    print(f"Computer: {losses}")
    print(f"Draws: {draws}")
    print(THIN_DIVIDER)


def show_final_score(wins: int, losses: int, draws: int):
    """Print the final score summary."""
    total = wins + losses + draws
    print(f"\n{DIVIDER}")
    print("FINAL SCORE".center(40))
    print(DIVIDER)
    print(f"\nYou:       {wins}")
    print(f"Computer:  {losses}")
    print(f"Draws:     {draws}")
    print(f"Rounds:    {total}")

    if total > 0:
        win_pct = (wins / total) * 100
        print(f"Win rate:  {win_pct:.1f}%")

    print()

    if wins > losses:
        print("You won the match!")
    elif losses > wins:
        print("Computer won the match!")
    else:
        print("The match ended in a tie!")

    print()


def ask_play_again() -> bool:
    """Ask the player if they want to play again. Returns True for yes."""
    while True:
        answer = input("\nPlay another round? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")


# ── Core game loop ──────────────────────────────────────────────────

def get_player_choice() -> str | None:
    """
    Prompt the player for a choice. Returns a normalized choice
    or None if the player wants to quit.
    """
    while True:
        show_menu()
        raw = input("\nYour choice: ")
        value = raw.strip().lower()

        if value in ("q", "quit", "exit"):
            return None

        if value in ("?", "rules", "help"):
            show_rules()
            continue

        normalized = normalize_input(raw)
        if normalized is not None:
            return normalized

        print("\nInvalid choice. Please choose rock, paper, or scissors (1-3).")


def play_round() -> tuple[str, str, str]:
    """
    Play a single round. Returns (player_choice, computer_choice, result).
    """
    player_choice = get_player_choice()
    if player_choice is None:
        return ("quit", "", "")

    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)

    return (player_choice, computer_choice, result)


def play_game():
    """Run the full game loop."""
    print(f"\n{DIVIDER}")
    print("ROCK PAPER SCISSORS".center(40))
    print(DIVIDER)
    print("\nRules:")
    print("  Rock beats Scissors")
    print("  Scissors beats Paper")
    print("  Paper beats Rock")
    print("  Same choice = Draw")

    wins = 0
    losses = 0
    draws = 0
    rounds_played = 0

    while True:
        player_choice, computer_choice, result = play_round()

        if player_choice == "quit":
            break

        rounds_played += 1

        # Display round outcome
        print(f"\n--- Round {rounds_played} ---")
        print(f"\nYou chose:      {player_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}\n")

        description = describe_round(player_choice, computer_choice, result)
        print(description)

        # Update scores
        if result == "player":
            wins += 1
        elif result == "computer":
            losses += 1
        else:
            draws += 1

        show_score(wins, losses, draws)

        # Ask to continue
        if not ask_play_again():
            break

    # Show final results if at least one round was played
    if rounds_played > 0:
        show_final_score(wins, losses, draws)
    else:
        print("\nThanks for playing! Maybe next time.\n")


# ── Entry point ──────────────────────────────────────────────────────

if __name__ == "__main__":
    play_game()
