"""
Tests for rock-paper-scissors game logic.
"""

import unittest
from game import normalize_input, determine_winner, get_computer_choice, describe_round, CHOICES, BEATS


class TestDetermineWinner(unittest.TestCase):
    """Test every combination of choices for winner determination."""

    def test_rock_vs_rock(self):
        self.assertEqual(determine_winner("rock", "rock"), "draw")

    def test_rock_vs_paper(self):
        self.assertEqual(determine_winner("rock", "paper"), "computer")

    def test_rock_vs_scissors(self):
        self.assertEqual(determine_winner("rock", "scissors"), "player")

    def test_paper_vs_rock(self):
        self.assertEqual(determine_winner("paper", "rock"), "player")

    def test_paper_vs_paper(self):
        self.assertEqual(determine_winner("paper", "paper"), "draw")

    def test_paper_vs_scissors(self):
        self.assertEqual(determine_winner("paper", "scissors"), "computer")

    def test_scissors_vs_rock(self):
        self.assertEqual(determine_winner("scissors", "rock"), "computer")

    def test_scissors_vs_paper(self):
        self.assertEqual(determine_winner("scissors", "paper"), "player")

    def test_scissors_vs_scissors(self):
        self.assertEqual(determine_winner("scissors", "scissors"), "draw")


class TestNormalizeInput(unittest.TestCase):
    """Test input normalization for all valid and invalid inputs."""

    # Valid string inputs
    def test_rock_lowercase(self):
        self.assertEqual(normalize_input("rock"), "rock")

    def test_paper_lowercase(self):
        self.assertEqual(normalize_input("paper"), "paper")

    def test_scissors_lowercase(self):
        self.assertEqual(normalize_input("scissors"), "scissors")

    # Uppercase
    def test_rock_uppercase(self):
        self.assertEqual(normalize_input("ROCK"), "rock")

    def test_paper_uppercase(self):
        self.assertEqual(normalize_input("PAPER"), "paper")

    def test_scissors_uppercase(self):
        self.assertEqual(normalize_input("SCISSORS"), "scissors")

    # Mixed case
    def test_rock_mixed_case(self):
        self.assertEqual(normalize_input("Rock"), "rock")

    def test_paper_mixed_case(self):
        self.assertEqual(normalize_input("PaPeR"), "paper")

    # Whitespace
    def test_rock_with_whitespace(self):
        self.assertEqual(normalize_input("  rock  "), "rock")

    def test_paper_with_whitespace(self):
        self.assertEqual(normalize_input("\tpaper\n"), "paper")

    # Number inputs
    def test_number_1(self):
        self.assertEqual(normalize_input("1"), "rock")

    def test_number_2(self):
        self.assertEqual(normalize_input("2"), "paper")

    def test_number_3(self):
        self.assertEqual(normalize_input("3"), "scissors")

    # Invalid inputs
    def test_empty_string(self):
        self.assertIsNone(normalize_input(""))

    def test_whitespace_only(self):
        self.assertIsNone(normalize_input("   "))

    def test_invalid_word(self):
        self.assertIsNone(normalize_input("banana"))

    def test_invalid_number(self):
        self.assertIsNone(normalize_input("4"))

    def test_negative_number(self):
        self.assertIsNone(normalize_input("-1"))

    def test_zero(self):
        self.assertIsNone(normalize_input("0"))

    def test_symbol(self):
        self.assertIsNone(normalize_input("!@#"))

    def test_single_letter_invalid(self):
        self.assertIsNone(normalize_input("a"))

    def test_partial_word(self):
        self.assertIsNone(normalize_input("rockk"))

    def test_r_shorthand(self):
        self.assertEqual(normalize_input("R"), "rock")

    def test_p_shorthand(self):
        self.assertEqual(normalize_input("P"), "paper")

    def test_s_shorthand(self):
        self.assertEqual(normalize_input("S"), "scissors")

    def test_r_lowercase_shorthand(self):
        self.assertEqual(normalize_input("r"), "rock")

    def test_p_lowercase_shorthand(self):
        self.assertEqual(normalize_input("p"), "paper")

    def test_s_lowercase_shorthand(self):
        self.assertEqual(normalize_input("s"), "scissors")


class TestComputerChoice(unittest.TestCase):
    """Test that computer choice is always valid."""

    def test_computer_always_chooses_valid(self):
        for _ in range(200):
            choice = get_computer_choice()
            self.assertIn(choice, CHOICES)

    def test_computer_can_pick_all_choices(self):
        """Over many rounds, the computer should pick each option at least once."""
        seen = set()
        for _ in range(500):
            seen.add(get_computer_choice())
        self.assertEqual(seen, set(CHOICES))


class TestDescribeRound(unittest.TestCase):
    """Test round description output."""

    def test_player_win_message(self):
        result = describe_round("rock", "scissors", "player")
        self.assertIn("Rock beats Scissors", result)
        self.assertIn("You win", result)

    def test_computer_win_message(self):
        result = describe_round("rock", "paper", "computer")
        self.assertIn("Paper beats Rock", result)
        self.assertIn("Computer wins", result)

    def test_draw_message(self):
        result = describe_round("paper", "paper", "draw")
        self.assertIn("draw", result.lower())

    def test_scissors_beats_paper(self):
        result = describe_round("scissors", "paper", "player")
        self.assertIn("Scissors beats Paper", result)


class TestGameConsistency(unittest.TestCase):
    """Cross-cutting consistency checks."""

    def test_beats_table_is_consistent(self):
        """Every entry in BEATS should point to a valid choice, and
        the reverse relationship should hold."""
        for choice, beaten in BEATS.items():
            self.assertIn(choice, CHOICES)
            self.assertIn(beaten, CHOICES)
            self.assertNotEqual(choice, beaten)
            # If A beats B, then B should not beat A
            self.assertNotEqual(BEATS.get(beaten), choice)

    def test_winner_returns_only_valid_results(self):
        for p in CHOICES:
            for c in CHOICES:
                result = determine_winner(p, c)
                self.assertIn(result, ("player", "computer", "draw"))


if __name__ == "__main__":
    unittest.main()
