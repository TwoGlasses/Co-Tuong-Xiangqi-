import unittest
import sys

sys.path.insert(0, '../')

from rule import Ruleset
from main import Game


class RulesetTest(unittest.TestCase):
    def test_is_in_board(self):
        game = Game()
        ruleset = Ruleset(game.board)

        # Testing the four corner of the board
        self.assertTrue(ruleset.is_in_board((0, 0)), "Upper left conner supposed to return True")
        self.assertTrue(ruleset.is_in_board((0, 8)), "Upper right conner supposed to return True")
        self.assertTrue(ruleset.is_in_board((9, 0)), "Lower left conner supposed to return True")
        self.assertTrue(ruleset.is_in_board((9, 8)), "Lower right conner supposed to return True")

        # Testing position outside of the board in four sides
        self.assertFalse(ruleset.is_in_board((0, 9)), "Outside of the right bound supposed to return False")
        self.assertFalse(ruleset.is_in_board((-1, -1)), "Negative position supposed to return False")
        self.assertFalse(ruleset.is_in_board((10, 0)), "Outside the lower bound supposed to return False")

    def test_is_in_upper_half(self):
        game = Game()
        ruleset = Ruleset(game.board)

        # Testing the four corner of the upper half
        self.assertTrue(ruleset.is_in_upper_half((0, 0)), "Upper left corner supposed to return True")
        self.assertTrue(ruleset.is_in_upper_half((0, 8)), "Upper right corner supposed to return True")
        self.assertTrue(ruleset.is_in_upper_half((4, 0)), "Lower left corner supposed to return True")
        self.assertTrue(ruleset.is_in_upper_half((4, 8)), "lower right corner supposed to return True")

        # Testing position that is not in upper half
        self.assertFalse(ruleset.is_in_upper_half((5, 0)), "Below left supposed to return Flase")
        self.assertFalse(ruleset.is_in_upper_half((5, 8)), "Below right supposed to return False")
        self.assertFalse(ruleset.is_in_upper_half((7, 7)), "A point in the lower half supposed to return False")
        self.assertFalse(ruleset.is_in_upper_half((10, 0)), "Below the board supposed to return False")
        self.assertFalse(ruleset.is_in_upper_half((4, 9)), "Outside the board to the right supposed to return False")
        self.assertFalse(ruleset.is_in_upper_half((-1, -1)), "Negative position supposed to return False")

    def test_is_in_lower_half(self):
        game = Game()
        ruleset = Ruleset(game.board)