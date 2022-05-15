# pylint: disable-all
# pylint: skip-file

"""
Lähes mahdotonta testata funktioita, kun ne eivät palauta mitään tai niissä on kiinni myös UI kamaa :/
"""
import unittest
import tkinter as TK
from class_yatzy import Yatzy, count_total
from class_dice import Dice
from class_scores import Scores
from class_updatescore import UpdateScore
import tkinter as TK
from tkinter import messagebox
import random

class TestYatzy(unittest.TestCase):
    def setUp(self):

        scorelist = [1, 2, 3, 4, 5, 6, "Kolme samaa", "Neljä samaa", "Full House",
        "Pieni suora", "Suuri suora", "Yatzy", "Sattuma"]
        self.top_score = 13
        self.bottom_score = 14
        self.values = [5,5,5,5,5]
        self.dice = []

        self.scores = {}
        for i in scorelist:
            self.scores[i] = 1
        self.temp_scores = {}
        for i in scorelist:
            self.temp_scores[i] = 0
        top_score = 55
        bonus = 0
        bottom_score = 50
        self.total = count_total(top_score, bonus, bottom_score)

    def count_total(self, i, j, k):
        pass
    def test_game_over_screen(self):
        """
        Tämä näkyy testin tehdessä testaajalle
        """
        self.assertEqual(Yatzy.game_over(self), None)

    def test_remaining_rolls_after_roll(self):
        self.remaining_rolls = 3
        Yatzy.remaining_rolls_roll(self)
        self.assertEqual(self.remaining_rolls, 2)
    
    def test_total_score(self):
        self.assertEqual(self.total, 105)

    def test_setting_hold_boolean_to_die(self):
        Dice.hold = TK.BooleanVar()
        Dice.number = TK.IntVar()
        Dice.set_hold_and_number(Dice,False, 5)
        self.assertEqual(Dice.hold.get(), False)

    def test_setting_die_number(self):
        Dice.hold = TK.BooleanVar()
        Dice.number = TK.IntVar()
        Dice.set_hold_and_number(Dice,False, 5)
        self.assertEqual(Dice.number.get(), 5)
