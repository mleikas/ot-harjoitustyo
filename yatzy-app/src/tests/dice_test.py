# pylint: disable-all
# pylint: skip-file
import unittest
import class_yatzy, class_dice, class_scores, class_updatescore
class TestDice(unittest.TestCase):
    def setup(self):
        self.remaining_rolls = 1

    def test_dice(self):
        self.assertEqual(Yatzy.roll, None)