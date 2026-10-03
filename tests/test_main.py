import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from main import play_game


class EndOfInputTests(unittest.TestCase):
    def run_game(self, inputs):
        output = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch(
            "main.get_computer_choice", return_value="scissors"
        ), redirect_stdout(output):
            play_game()
        return output.getvalue()

    def test_eof_at_first_choice(self):
        output = self.run_game([EOFError()])
        self.assertIn("Goodbye!", output)
        self.assertNotIn("FINAL SCORE", output)

    def test_eof_at_replay_preserves_score(self):
        output = self.run_game(["rock", EOFError()])
        self.assertIn("FINAL SCORE", output)
        self.assertIn("You:           1", output)
        self.assertIn("Rounds:        1", output)

    def test_eof_at_later_choice_preserves_score(self):
        output = self.run_game(["rock", "y", EOFError()])
        self.assertIn("Rounds:        1", output)
        self.assertIn("Goodbye!", output)
