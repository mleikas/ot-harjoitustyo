import unittest
from main import Yatzy, Dice, Scores, UpdateScore
class TestDice(unittest.TestCase):
    def setup(self):
        print("ermm yeah")

    def test_dice_generate_five_numbers(self):
        self.assertEqual(len(generaterandom()), 5)